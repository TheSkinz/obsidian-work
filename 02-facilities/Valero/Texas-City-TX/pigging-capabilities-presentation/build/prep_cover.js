// Cover photo -> img/cover_trimax.jpg (right-hand panel, 8.333 x 7.5 in, left edge faded to the slide charcoal).
// Source: the front-closest Trimax shot from the LAR presentation photos (IMG_1973, 2560 x 1438).
const sharp = require('sharp');
const SRC = 'C:/Users/Jwuts/OneDrive/USADeBusk/Facilities/Marathon/Marathon Carson RFQ/_Presentation photos/IMG_1973-UPDATED-USADEBUSK-scaled.jpg';
const O = __dirname + '/img/';

(async () => {
  // Crop out most of the pavement below the rig (rig bottom is ~y 1150 of 1438).
  const H = 1300, W = Math.round(H * 8.333 / 7.5); // 1444
  const left = 230, top = 0;                        // control-house end and trailer midsection in frame
  const photo = await sharp(SRC).extract({ left, top, width: W, height: H }).modulate({ saturation: 1.05 }).toBuffer();
  const fade = Buffer.from(`<svg xmlns='http://www.w3.org/2000/svg' width='${W}' height='${H}'><defs><linearGradient id='g' x1='0' y1='0' x2='1' y2='0'><stop offset='0' stop-color='#1E1E1E' stop-opacity='1'/><stop offset='0.12' stop-color='#1E1E1E' stop-opacity='0'/></linearGradient></defs><rect width='100%' height='100%' fill='url(#g)'/></svg>`);
  await sharp(photo).composite([{ input: fade }]).jpeg({ quality: 86 }).toFile(O + 'cover_trimax.jpg');
  console.log('cover done', W, H);
})();
