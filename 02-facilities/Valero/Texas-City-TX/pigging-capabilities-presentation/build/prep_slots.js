// Tall side-panel photo for the methodology slide -> img/slot_method_t6.jpg
// Source: trimax6.jpg in the LAR build (a photo not used elsewhere in this deck).
const sharp = require('sharp');
const SRC = __dirname + '/../../../../Marathon/Carson-CA/DSP26098-technical-presentation/build/img/trimax6.jpg';
const O = __dirname + '/img/';
const PPI = 200;

(async () => {
  const W = Math.round(4.0 * PPI), H = Math.round(7.5 * PPI);
  const bg = await sharp(SRC).resize(W, H, { fit: 'cover' }).blur(45).modulate({ brightness: 0.5 }).toBuffer();
  const fg = await sharp(SRC).resize(W, H, { fit: 'inside' }).toBuffer({ resolveWithObject: true });
  const top = Math.round((H - fg.info.height) / 2);
  await sharp(bg).composite([{ input: fg.data, left: 0, top }]).jpeg({ quality: 84 }).toFile(O + 'slot_method_t6.jpg');
  console.log('slot done');
})();
