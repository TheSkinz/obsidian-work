// Photo crops for slide panels and cards. Each photo is used on one slide only;
// trimax6.jpg in the LAR build is the same shot as card_ready, so it is not used.
const sharp = require('sharp');
const O = __dirname + '/img/';

(async () => {
  // Services side panel (4.0 x 7.5 in): the rig at a heater, cropped to drop the empty concrete foreground.
  // src/onsite_heater.jpg is 1206 x 1792; the rig sits at x 290-900, y 980-1390.
  const ch = 1450, cw = Math.round(ch * 4.0 / 7.5); // 773
  await sharp(__dirname + '/src/onsite_heater.jpg').extract({ left: 215, top: 0, width: cw, height: ch }).jpeg({ quality: 86 }).toFile(O + 'services_heater.jpg');

  // Closing slide card (16:9): the road-shot rig and tractor on a night terminal background.
  // src/road_night.jpg is Jesse's AI background replacement of src/road.jpg (2026-10-13): the rig is the real
  // photo; only the background and lighting are generated. The fully generated variants were rejected.
  await sharp(__dirname + '/src/road_night.jpg').resize(1600, 900, { fit: 'cover' }).jpeg({ quality: 88 }).toFile(O + 'why_road.jpg');
  // Landscape cards replacing blur-filled side panels, so the rig fills the frame.
  const LAR = __dirname + '/../../../../Marathon/Carson-CA/DSP26098-technical-presentation/build/img/';
  await sharp(LAR + 'hero.jpg').jpeg({ quality: 86 }).toFile(O + 'card_diff.jpg');             // derricks, 16:9
  // card_ready.jpg (TriMax 4, IMG_1973) is made in prep_cover.js. The TriMax 6 shot now lives on the cover.
  console.log('slots done');
})();
