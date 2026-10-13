// US map with Valero reference sites -> img/valero_map.png
// Run with NODE_PATH pointing at the installed deps (see README).
const fs = require('fs');
const sharp = require('sharp');
const d3 = require('d3-geo');
const topo = require('topojson-client');
const O = __dirname + '/img/';

(async () => {
  const us = JSON.parse(fs.readFileSync(require.resolve('us-atlas/states-albers-10m.json')));
  const states = topo.feature(us, us.objects.states);
  const nation = topo.mesh(us, us.objects.states, (a, b) => a !== b);
  const path = d3.geoPath();
  const proj = d3.geoAlbersUsa().scale(1300).translate([487.5, 305]);
  // [label, lat, lon, label dx, label dy, anchor]. Starred sites await confirmation before release.
  const sites = [
    ['Benicia, CA', 38.07, -122.14, 11, 4.5, 'start'],
    ['Wilmington, CA', 33.79, -118.24, 11, 4.5, 'start'],
    ['McKee (Sunray), TX', 35.96, -101.86, -11, 4.5, 'end'],
    ['Oklahoma City, OK*', 35.47, -97.52, 11, -2, 'start'],
    ['Ardmore, OK', 34.17, -97.13, 11, 8, 'start'],
    ['Memphis, TN', 35.08, -90.09, 11, 4.5, 'start'],
    ['Three Rivers, TX', 28.46, -98.18, -11, 4.5, 'end'],
    ['Corpus Christi East & West, TX', 27.81, -97.42, -11, 10, 'end'],
    ['Houston, TX*', 29.72, -95.25, -70, -48, 'end'],
    ['Port Arthur, TX (incl. DGD*)', 29.87, -93.93, 30, -52, 'start'],
    ['St. Charles & DGD*, Norco, LA', 29.99, -90.41, 40, -86, 'start'],
    ['Meraux, LA', 29.93, -89.92, 34, 30, 'start'],
  ];
  let pins = '';
  for (const [name, lat, lon, dx, dy, anchor] of sites) {
    const [x, y] = proj([lon, lat]);
    const far = Math.abs(dx) > 20 || Math.abs(dy) > 20;
    if (far) pins += `<line x1="${x}" y1="${y}" x2="${x + dx}" y2="${y + dy + (dy < 0 ? 4 : -10)}" stroke="#FCC30A" stroke-width="1.5"/>`;
    pins += `<circle cx="${x}" cy="${y}" r="6.5" fill="#FCC30A" stroke="#1E1E1E" stroke-width="2"/><text x="${x + dx}" y="${y + dy}" font-family="Arial" font-size="13.5" font-weight="bold" fill="#FFFFFF" stroke="#1E1E1E" stroke-width="4" paint-order="stroke" text-anchor="${anchor}">${name.replace(/&/g, '&amp;')}</text>`;
  }
  const t = proj([-94.93, 29.38]);
  const target = `<circle cx="${t[0]}" cy="${t[1]}" r="17" fill="none" stroke="#FFFFFF" stroke-width="2" stroke-dasharray="4 3"/><circle cx="${t[0]}" cy="${t[1]}" r="8" fill="#FFFFFF"/><line x1="${t[0] + 6}" y1="${t[1] + 16}" x2="${t[0] + 22}" y2="${t[1] + 34}" stroke="#FFFFFF" stroke-width="1.5"/><text x="${t[0] + 18}" y="${t[1] + 50}" font-family="Arial" font-size="15" font-weight="bold" fill="#FCC30A" stroke="#1E1E1E" stroke-width="4" paint-order="stroke" text-anchor="start">Texas City</text>`;
  const svg = `<svg xmlns="http://www.w3.org/2000/svg" width="930" height="600" viewBox="20 10 930 600">
    <g fill="#343434" stroke="none">${states.features.filter(f => !['02', '15'].includes(f.id)).map(f => `<path d="${path(f)}"/>`).join('')}</g>
    <path d="${path(nation)}" fill="none" stroke="#1E1E1E" stroke-width="1.2"/>
    ${pins}${target}</svg>`;
  await sharp(Buffer.from(svg), { density: 200 }).resize(1860, 1200).png().toFile(O + 'valero_map.png');
  console.log('map done');
})();
