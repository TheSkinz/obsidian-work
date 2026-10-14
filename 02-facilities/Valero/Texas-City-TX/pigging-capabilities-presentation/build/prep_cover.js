// Cover photo and the readiness card.
// cover_night.jpg: src/trimax6_night.jpg is Jesse's AI background replacement of the real TriMax 6 photo
// (2026-10-13). The rig is real; only the night tank-farm background is generated. Full slide width, top edge
// faded into the slide charcoal so the title can sit over the sky.
// card_ready.jpg: the real front-closest TriMax 4 shot (IMG_1973), cropped to the whole rig.
const sharp = require('sharp');
const O = __dirname + '/img/';
const IMG1973 = 'C:/Users/Jwuts/OneDrive/USADeBusk/Facilities/Marathon/Marathon Carson RFQ/_Presentation photos/IMG_1973-UPDATED-USADEBUSK-scaled.jpg';

(async () => {
  const src = __dirname + '/src/trimax6_night.jpg';
  const { width: W, height: H } = await sharp(src).metadata();
  const fade = Buffer.from(`<svg xmlns='http://www.w3.org/2000/svg' width='${W}' height='${H}'><defs><linearGradient id='g' x1='0' y1='0' x2='0' y2='1'><stop offset='0' stop-color='#1E1E1E' stop-opacity='1'/><stop offset='0.22' stop-color='#1E1E1E' stop-opacity='0'/></linearGradient></defs><rect width='100%' height='100%' fill='url(#g)'/></svg>`);
  await sharp(src).composite([{ input: fade }]).jpeg({ quality: 88 }).toFile(O + 'cover_night.jpg');

  // IMG_1973 is 2560 x 1438; the rig spans x ~218-1946, y ~330-1150. Crop at the card's 920:434 aspect.
  const cw = 1760, ch = Math.round(cw * 434 / 920); // 830
  await sharp(IMG1973).extract({ left: 200, top: 320, width: cw, height: ch }).jpeg({ quality: 88 }).toFile(O + 'card_ready.jpg');
  console.log('cover done', W, H);
})();
