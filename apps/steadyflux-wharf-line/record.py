"""Record a curated clip of the wharf-line page with Playwright (headed Chromium, real GPU), then encode to MP4.
Usage: python record.py <url> <out.mp4>
"""
import sys, time, pathlib, subprocess, shutil
from playwright.sync_api import sync_playwright
import imageio_ffmpeg

url, out = sys.argv[1], pathlib.Path(sys.argv[2])
W, H = 1920, 1080
vdir = out.parent / 'vid'; shutil.rmtree(vdir, ignore_errors=True); vdir.mkdir()

# (seek_seconds, hold_seconds): overview, 8-in tunnels, GW-59 cluster, P-1 approach + hold, closing
SHOTS = [(0.5, 4.5), (97, 13.5), (167, 3.5)]

with sync_playwright() as p:
    b = p.chromium.launch(channel='chrome', headless=False, args=['--use-angle=default', '--enable-gpu-rasterization', f'--window-size={W},{H+90}', '--hide-scrollbars'])
    ctx = b.new_context(viewport={'width': W, 'height': H}, device_scale_factor=1, record_video_dir=str(vdir), record_video_size={'width': W, 'height': H})
    page = ctx.new_page()
    page.goto(url, wait_until='load')
    page.wait_for_function('window.__ws && window.__ws.tNow() >= 0')
    time.sleep(1.5)
    for t, hold in SHOTS:
        page.evaluate(f'window.__ws.seek({t})')
        time.sleep(hold)
    page.evaluate('window.__ws.pause()')
    time.sleep(0.5)
    ctx.close(); b.close()

webm = next(vdir.glob('*.webm'))
ff = imageio_ffmpeg.get_ffmpeg_exe()
# trim the first 1.5 s of load, encode h264 for phones, faststart for instant playback
subprocess.run([ff, '-y', '-ss', '1.5', '-i', str(webm), '-vf', f'scale={W}:{H},fps=30,format=yuv420p', '-c:v', 'libx264', '-preset', 'medium', '-crf', '20', '-movflags', '+faststart', '-an', str(out)], check=True)
print(out, out.stat().st_size, 'bytes')
