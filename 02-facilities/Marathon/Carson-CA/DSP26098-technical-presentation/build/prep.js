const sharp = require('sharp');
const fs = require('fs');
const topo = require('topojson-client');
const d3 = require('d3-geo');
const U = '/root/.claude/uploads/c8998718-f22f-57a3-84c2-766db1d92b4c/';
const S = '/tmp/claude-0/-home-user-obsidian-work/c8998718-f22f-57a3-84c2-766db1d92b4c/scratchpad/';
const O = S + 'deck/img/';

(async () => {
  // Photos: 16:9 crops at 1920x1080, plus a portrait panel crop
  await sharp(U + '0ca4a2dd-image.jpg').rotate().resize(1920, 1080, { fit: 'cover', position: 'south' }).modulate({ brightness: 1.0, saturation: 1.05 }).jpeg({ quality: 82 }).toFile(O + 'hero.jpg');
  await sharp(U + '4af2e311-image.jpg').rotate().resize(1920, 1080, { fit: 'cover', position: 'center' }).modulate({ brightness: 1.12 }).linear(1.08, -6).jpeg({ quality: 82 }).toFile(O + 'onsite_wide.jpg');
  await sharp(U + '4af2e311-image.jpg').rotate().resize(900, 1080, { fit: 'cover', position: 'south' }).modulate({ brightness: 1.12 }).linear(1.08, -6).jpeg({ quality: 82 }).toFile(O + 'onsite_tall.jpg');
  await sharp(U + '595a3d36-image.jpg').rotate().resize(1920, 1080, { fit: 'cover', position: 'center' }).jpeg({ quality: 82 }).toFile(O + 'trimax1.jpg');
  await sharp(U + '87eca82b-image.jpg').rotate().resize(1200, 900, { fit: 'cover', position: 'center' }).modulate({ brightness: 1.05 }).jpeg({ quality: 80 }).toFile(O + 'trimax6.jpg');
  await sharp(U + '0ca4a2dd-image.jpg').rotate().resize(1000, 1080, { fit: 'cover', position: 'center' }).jpeg({ quality: 82 }).toFile(O + 'hero_tall.jpg');

  // Gradient overlays (dark left -> transparent right), and a bottom fade
  const grad = (w, h, stops, dir) => Buffer.from(`<svg xmlns="http://www.w3.org/2000/svg" width="${w}" height="${h}"><defs><linearGradient id="g" ${dir}>${stops}</linearGradient></defs><rect width="100%" height="100%" fill="url(#g)"/></svg>`);
  await sharp(grad(1920, 1080, '<stop offset="0" stop-color="#111" stop-opacity="0.94"/><stop offset="0.45" stop-color="#111" stop-opacity="0.78"/><stop offset="0.75" stop-color="#111" stop-opacity="0.15"/><stop offset="1" stop-color="#111" stop-opacity="0"/>', 'x1="0" y1="0" x2="1" y2="0"')).png().toFile(O + 'fade_left.png');
  await sharp(grad(1920, 1080, '<stop offset="0" stop-color="#111" stop-opacity="0.15"/><stop offset="0.55" stop-color="#111" stop-opacity="0.55"/><stop offset="1" stop-color="#111" stop-opacity="0.95"/>', 'x1="0" y1="0" x2="0" y2="1"')).png().toFile(O + 'fade_bottom.png');

  // Reversed logo: dark grey glyphs -> white, keep gold
  const { data, info } = await sharp('/home/user/obsidian-work/assets/brand/usadebusk-logo.png').ensureAlpha().raw().toBuffer({ resolveWithObject: true });
  for (let i = 0; i < data.length; i += 4) {
    const [r, g, b] = [data[i], data[i + 1], data[i + 2]];
    if (Math.abs(r - g) < 25 && Math.abs(g - b) < 25 && r < 140) { data[i] = data[i + 1] = data[i + 2] = 255; }
  }
  await sharp(data, { raw: info }).png().toFile(O + 'logo_white.png');
  fs.copyFileSync('/home/user/obsidian-work/assets/brand/usadebusk-logo.png', O + 'logo.png');

  // CARB cert thumbnails
  for (const [src, out] of [[S + 'certs/t1_r1.png', 'cert_t1.png'], [S + 'certs/t2_p2_0.png', 'cert_t2.png'], [S + 'certs/t6_r3.png', 'cert_t6.png']]) {
    await sharp(src).resize(600, 780, { fit: 'contain', background: '#ffffff' }).flatten({ background: '#ffffff' }).png().toFile(O + out);
  }

  // US map with MPC reference sites
  const us = JSON.parse(fs.readFileSync('node_modules/us-atlas/states-albers-10m.json'));
  const states = topo.feature(us, us.objects.states);
  const nation = topo.mesh(us, us.objects.states, (a, b) => a !== b);
  const path = d3.geoPath();
  const proj = d3.geoAlbersUsa().scale(1300).translate([487.5, 305]);
  const sites = [
    ['Martinez, CA', 38.02, -122.13, 'r'], ['Salt Lake City, UT', 40.76, -111.89, 'r'], ['Dickinson, ND', 46.88, -102.79, 'r'],
    ['St. Paul Park, MN', 44.84, -92.99, 'r'], ['Detroit, MI', 42.29, -83.16, 'r'], ['Robinson, IL', 39.01, -87.74, 'l'],
    ['Catlettsburg, KY', 38.40, -82.60, 'r'], ['Garyville, LA', 30.06, -90.62, 'r'], ['Galveston Bay, TX', 29.38, -94.90, 'l'],
  ];
  const lar = proj([-118.23, 33.81]);
  let pins = '';
  for (const [name, lat, lon, side] of sites) {
    const [x, y] = proj([lon, lat]);
    const tx = side === 'r' ? x + 11 : x - 11; const anchor = side === 'r' ? 'start' : 'end';
    pins += `<circle cx="${x}" cy="${y}" r="6.5" fill="#FCC30A" stroke="#1E1E1E" stroke-width="2"/><text x="${tx}" y="${y + 4.5}" font-family="Arial" font-size="13.5" font-weight="bold" fill="#FFFFFF" stroke="#1E1E1E" stroke-width="4" paint-order="stroke" text-anchor="${anchor}">${name}</text>`;
  }
  const larPin = `<circle cx="${lar[0]}" cy="${lar[1]}" r="17" fill="none" stroke="#FFFFFF" stroke-width="2" stroke-dasharray="4 3"/><circle cx="${lar[0]}" cy="${lar[1]}" r="8" fill="#FFFFFF"/><text x="${lar[0] + 22}" y="${lar[1] + 26}" font-family="Arial" font-size="15" font-weight="bold" fill="#FCC30A" stroke="#1E1E1E" stroke-width="4" paint-order="stroke">LAR: Carson &amp; Wilmington</text>`;
  const svg = `<svg xmlns="http://www.w3.org/2000/svg" width="930" height="580" viewBox="20 10 930 580">
    <g fill="#343434" stroke="none">${states.features.filter(f=>!['02','15'].includes(f.id)).map(f => `<path d="${path(f)}"/>`).join('')}</g>
    <path d="${path(nation)}" fill="none" stroke="#1E1E1E" stroke-width="1.2"/>
    ${larPin}${pins}</svg>`;
  await sharp(Buffer.from(svg), { density: 200 }).resize(1860, 1160).png().toFile(O + 'mpc_map.png');
  console.log('prep done');
})();
