const sharp = require('sharp');
const U = '/root/.claude/uploads/c8998718-f22f-57a3-84c2-766db1d92b4c/';
const O = __dirname + '/img/';
const PPI = 200;

async function fitBlur(srcBuf, wIn, hIn, anchor, out, fgTweak = s => s) {
  let W = Math.round(wIn * PPI), H = Math.round(hIn * PPI);
  if (W > 2667) { H = Math.round(H * 2667 / W); W = 2667; }
  const bg = await sharp(srcBuf).resize(W, H, { fit: 'cover' }).blur(45).modulate({ brightness: 0.5 }).toBuffer();
  const fg = await fgTweak(sharp(srcBuf).resize(W, H, { fit: 'inside' })).toBuffer({ resolveWithObject: true });
  const fw = fg.info.width, fh = fg.info.height;
  let left = Math.round((W - fw) / 2), top = Math.round((H - fh) / 2);
  if (anchor === 'right') left = W - fw;
  if (anchor === 'bottom') top = H - fh;
  await sharp(bg).composite([{ input: fg.data, left, top }]).jpeg({ quality: 84 }).toFile(O + out);
  console.log(out, W, H, 'fg', fw, fh);
}

(async () => {
  const hero = await sharp(U + '0ca4a2dd-image.jpg').rotate().toBuffer();
  const onsite = await sharp(U + '4af2e311-image.jpg').rotate().toBuffer();
  const onsiteLift = s => s.modulate({ brightness: 1.12 }).linear(1.08, -6);
  const trimax1 = await sharp(U + '595a3d36-image.jpg').rotate().toBuffer();
  const road = await sharp(U + '32d9289f-image.jpg').rotate().extract({ left: 0, top: 0, width: 1178, height: 886 }).toBuffer();
  const danger = await sharp(__dirname + '/../brochure/img_p2_2.jpeg').toBuffer();

  await fitBlur(hero, 13.333, 7.5, 'right', 'slot_title.jpg');
  await fitBlur(onsite, 4.4, 7.5, 'bottom', 'slot_agenda.jpg', onsiteLift);
  await fitBlur(onsite, 4.0, 7.5, 'bottom', 'slot_method.jpg', onsiteLift);
  await fitBlur(trimax1, 4.6, 7.5, 'center', 'slot_ready.jpg');
  await fitBlur(trimax1, 13.333, 7.5, 'right', 'slot_trimax.jpg');
  await fitBlur(road, 13.333, 7.5, 'right', 'slot_road.jpg', s => s.sharpen());
  await fitBlur(danger, 3.9, 7.5, 'bottom', 'slot_danger.jpg');
  await fitBlur(hero, 4.0, 7.5, 'center', 'slot_diff.jpg');
  await fitBlur(hero, 13.333, 7.5, 'right', 'slot_why.jpg');
  await fitBlur(onsite, 13.333, 7.5, 'center', 'slot_qa.jpg', onsiteLift);
  const heroSq = await sharp(U + '5d424d3f-image.jpg').rotate().toBuffer();
  const onsiteSq = await sharp(U + '03fe455a-image.jpg').rotate().toBuffer();
  const t6crop = await sharp(U + '09fb8d3c-image.jpg').rotate().toBuffer();
  const t1crop = await sharp(U + 'bc9f41ad-image.jpg').rotate().toBuffer();
  const road2 = await sharp(U + '82a37543-image.jpg').rotate().extract({ left: 0, top: 0, width: 1186, height: 714 }).toBuffer();
  await fitBlur(t1crop, 4.4, 7.5, 'center', 'slot_agenda.jpg');
  await fitBlur(onsiteSq, 4.0, 7.5, 'center', 'slot_method.jpg');
  await fitBlur(t6crop, 4.6, 7.5, 'center', 'slot_ready.jpg');
  await fitBlur(t1crop, 13.333, 7.5, 'right', 'slot_trimax.jpg');
  await fitBlur(road2, 13.333, 7.5, 'right', 'slot_road.jpg', s => s.sharpen());
  await fitBlur(heroSq, 4.0, 7.5, 'center', 'slot_diff.jpg');
  await fitBlur(onsiteSq, 13.333, 7.5, 'center', 'slot_qa.jpg');
  const lar = await sharp(U + '3be70373-image.png').flatten({ background: '#000' }).toBuffer();
  await fitBlur(lar, 4.0, 7.5, 'center', 'slot_lar.jpg');
  await fitBlur(heroSq, 13.333, 7.5, 'right', 'slot_title.jpg');
  await fitBlur(heroSq, 13.333, 7.5, 'right', 'slot_why.jpg');
  const shop = await sharp(U + '9711342e-image.jpg').rotate().toBuffer();
  await fitBlur(shop, 13.333, 7.5, 'center', 'slot_shop.jpg', x => x.modulate({ brightness: 1.25 }).gamma(1.25));
  await sharp(Buffer.from(`<svg xmlns='http://www.w3.org/2000/svg' width='1920' height='1080'><defs><linearGradient id='g' x1='0' y1='0' x2='0' y2='1'><stop offset='0' stop-color='#111' stop-opacity='0'/><stop offset='0.62' stop-color='#111' stop-opacity='0'/><stop offset='1' stop-color='#111' stop-opacity='0.85'/></linearGradient></defs><rect width='100%' height='100%' fill='url(#g)'/></svg>`)).png().toFile(O + 'fade_bottom_light.png');
})();
