// MPC LAR Heater Pigging & Decoking — Technical Proposal presentation (DSP#26098)
const pptxgen = require('pptxgenjs');
const React = require('react');
const ReactDOMServer = require('react-dom/server');
const sharp = require('sharp');
const fa = require('react-icons/fa');

const IMG = __dirname + '/img/';
const PCW = 1748, PCH = 1090;
const C = {
  dark: '1E1E1E', char: '2B2B2B', char2: '363636', gold: 'FCC30A', white: 'FFFFFF',
  light: 'F4F4F4', text: '222222', muted: '5E5E5E', soft: 'BDBDBD', rule: 'DDDDDD', grey: '8A8A8A',
};
const FONT = 'Arial';
const W = 13.333, H = 7.5;

async function icon(name, color, size = 256) {
  const svg = ReactDOMServer.renderToStaticMarkup(React.createElement(fa[name], { color: '#' + color, size: String(size) }));
  const buf = await sharp(Buffer.from(svg)).png().toBuffer();
  return 'image/png;base64,' + buf.toString('base64');
}

(async () => {
  const pres = new pptxgen();
  pres.layout = 'LAYOUT_WIDE';
  pres.author = 'USA DeBusk';
  pres.company = 'USA DeBusk, LLC';
  pres.title = 'LAR Heater Pigging & Decoking Services — Technical Proposal';

  // ---------- helpers ----------
  const txt = (slide, text, o) => slide.addText(text, Object.assign({ fontFace: FONT, isTextBox: true, margin: 0 }, o));

  const chip = (slide, num, label, dark, cx = 0.6) => {
    const t = num ? `${num}   ${label.toUpperCase()}` : label.toUpperCase();
    const AW = { ' ': 278, '&': 722, ',': 278, '/': 278, '-': 333, '.': 278, A: 722, B: 722, C: 722, D: 722, E: 667, F: 611, G: 778, H: 722, I: 278, J: 556, K: 722, L: 611, M: 833, N: 722, O: 778, P: 667, Q: 778, R: 722, S: 667, T: 611, U: 722, V: 667, W: 944, X: 667, Y: 667, Z: 611 };
    const tw = [...t].reduce((a, ch) => a + (AW[ch] || 556), 0) / 1000 * 10.5 / 72 + t.length * 1.5 / 72;
    const w = tw + 0.4;
    slide.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: cx, y: 0.45, w, h: 0.34, fill: { color: C.gold }, line: { color: C.gold }, rectRadius: 0.08 });
    txt(slide, t, { x: cx, y: 0.45, w, h: 0.34, fontSize: 10.5, bold: true, color: C.dark, align: 'center', valign: 'middle', charSpacing: 1.5 });
  };

  const title = (slide, t, dark, o = {}) => txt(slide, t, Object.assign({ x: 0.6, y: 0.92, w: 12.1, h: 0.8, fontSize: 32, bold: true, color: dark ? C.white : C.text, valign: 'top' }, o));
  const sub = (slide, t, dark, o = {}) => txt(slide, t, Object.assign({ x: 0.6, y: 1.62, w: 12.1, h: 0.4, fontSize: 15, color: dark ? C.soft : C.muted, valign: 'top' }, o));

  const footer = (slide, dark, fx = 0.6) => {
    const pageNo = pres._slides.length - 1;
    txt(slide, 'USA DeBusk  |  LAR Heater Pigging & Decoking Services  |  DSP#26098', { x: fx, y: 7.02, w: 8, h: 0.25, fontSize: 9, color: dark ? C.soft : '9A9A9A' });
    txt(slide, String(pageNo + 1), { x: 12.2, y: 7.02, w: 0.53, h: 0.25, fontSize: 9, color: dark ? C.soft : '9A9A9A', align: 'right' });
  };

  const bg = (slide, color) => { slide.background = { color }; };

  const shadow = () => ({ type: 'outer', color: '000000', blur: 8, offset: 2, angle: 90, opacity: 0.12 });

  const iconCircle = async (slide, name, x, y, d, circleColor, iconColor) => {
    slide.addShape(pres.shapes.OVAL, { x, y, w: d, h: d, fill: { color: circleColor }, line: { color: circleColor } });
    const pad = d * 0.25;
    slide.addImage({ data: await icon(name, iconColor), x: x + pad, y: y + pad, w: d - 2 * pad, h: d - 2 * pad });
  };

  // =====================================================================
  // 1. TITLE
  {
    const s = pres.addSlide();
    bg(s, C.dark);
    s.addImage({ path: IMG + 'slot_title.jpg', x: 0, y: 0, w: W, h: H });
    s.addImage({ path: IMG + 'fade_left.png', x: 0, y: 0, w: W, h: H });
    s.addImage({ path: IMG + 'logo_white.png', x: 0.7, y: 0.65, w: 3.4, h: 3.4 * 101 / 674 });
    txt(s, 'LAR Heater Pigging\n& Decoking Services', { x: 0.7, y: 2.35, w: 7.2, h: 1.9, fontSize: 44, bold: true, color: C.white, valign: 'top', lineSpacingMultiple: 0.95 });
    txt(s, 'Marathon Petroleum, Los Angeles Refinery', { x: 0.7, y: 4.3, w: 7.2, h: 0.45, fontSize: 20, color: C.gold, bold: true });
    txt(s, 'Carson Coker #1 & #2, Wilmington DCU H-101', { x: 0.7, y: 4.78, w: 7.2, h: 0.4, fontSize: 16, color: C.soft });
    txt(s, [
      { text: 'Presented by Marshall Douglas', options: { bold: true, color: C.white, breakLine: true } },
      { text: 'Director of Pigging Operations', options: { color: C.soft, breakLine: true } },
      { text: 'DSP#26098  |  September 2026', options: { color: C.grey } },
    ], { x: 0.7, y: 5.75, w: 7, h: 1.0, fontSize: 13, valign: 'top', paraSpaceAfter: 2 });
    s.addNotes(`[~1 min] Open: thank the evaluation team for the shortlist. Introduce yourself (Marshall Douglas, Director of Pigging Operations) and anyone attending with you.
Frame: "This deck follows your ten discussion points in your order, so you can score as we go. We'll hold about 40 minutes and leave 20 for questions."
The photo is our TriMax triple pumper on a delayed coker, the same service we're proposing for LAR.`);
  }

  // =====================================================================
  // 2. AGENDA
  {
    const s = pres.addSlide();
    bg(s, C.dark);
    s.addImage({ path: IMG + 'slot_agenda.jpg', x: 0, y: 0, w: 4.4, h: H });
    txt(s, 'Agenda', { x: 5.0, y: 0.6, w: 7, h: 0.7, fontSize: 34, bold: true, color: C.white });
    txt(s, "Structured to the evaluation team's ten discussion points", { x: 5.0, y: 1.3, w: 7.5, h: 0.4, fontSize: 15, color: C.soft });
    const items = ['Pigging & decoking methodology', 'Execution plan & schedule', 'Operational readiness & resources', 'Equipment & technology', 'Cleanliness verification & QA/QC',
      'Emergency response & local resources', 'Safety & risk mitigation', 'Best practices, capabilities & innovation', 'MPC references & case studies', 'Why USA DeBusk'];
    items.forEach((it, i) => {
      const col = i < 5 ? 0 : 1, row = i % 5;
      const x = 5.0 + col * 4.1, y = 2.2 + row * 0.9;
      txt(s, String(i + 1).padStart(2, '0'), { x, y, w: 0.75, h: 0.6, fontSize: 26, bold: true, color: C.gold, valign: 'middle' });
      txt(s, it, { x: x + 0.8, y, w: 3.15, h: 0.6, fontSize: 15, color: C.white, valign: 'middle' });
    });
    s.addNotes(`[~1 min] Walk the agenda quickly. Point out it mirrors MPC's list 1 to 10. Item 10 "Others" is used as a closing summary.
Transition: "Let's start with what we understood the job to be."`);
  }

  // =====================================================================
  // 3. SCOPE UNDERSTANDING
  {
    const s = pres.addSlide();
    bg(s, C.white);
    s.addImage({ path: IMG + 'slot_lar.jpg', x: 9.33, y: 0, w: 4.0, h: H });
    txt(s, 'Marathon Los Angeles Refinery\nCarson delayed coker', { x: 9.53, y: 5.9, w: 3.6, h: 0.5, fontSize: 11, bold: true, color: C.white, align: 'center', valign: 'top' });
    txt(s, 'Photo: Marathon Petroleum', { x: 9.53, y: 6.45, w: 3.6, h: 0.25, fontSize: 9, color: C.soft, align: 'center' });
    chip(s, null, 'Scope', false);
    title(s, 'Our understanding of the scope', false, { w: 8.3 });
    sub(s, 'Recurring mechanical pigging & decoking, lump sum per occurrence, mobilization and demobilization waived', false, { w: 8.2, h: 0.7 });
    const hdr = (t) => ({ text: t, options: { bold: true, color: C.white, fill: { color: C.dark }, fontSize: 12 } });
    const rows = [
      [hdr('Unit'), hdr('Heater'), hdr('Passes'), hdr('Per year'), hdr('5 years')],
      ['Carson Coker #1', 'Heater #1', '2', '4', '20'],
      ['Carson Coker #1', 'Heater #2', '2', '4', '20'],
      ['Carson Coker #2', 'Heater #3', '2', '3', '15'],
      ['Wilmington DCU', 'H-101', '4', '1', '5'],
    ].map((r, i) => i === 0 ? r : r.map(c => ({ text: c, options: { fill: { color: i % 2 ? C.white : 'F7F7F7' }, color: C.text, fontSize: 13 } })));
    s.addTable(rows, { x: 0.6, y: 2.45, w: 7.2, colW: [2.1, 1.5, 1.1, 1.25, 1.25], rowH: 0.52, fontFace: FONT, border: { type: 'solid', pt: 0.75, color: C.rule }, valign: 'middle' });
    txt(s, 'Source: DSP#26098 Rev 1, scope table', { x: 0.6, y: 5.12, w: 7.2, h: 0.3, fontSize: 10, color: C.grey, italic: true });
    const tiles = [['4', 'heaters, two sites'], ['12', 'decokes per year'], ['60', 'decokes over 5 years'], ['2,790', 'project hours, 5 years']];
    tiles.forEach(([n, l], i) => {
      const x = 0.6 + i * 2.05, y = 5.5;
      s.addShape(pres.shapes.RECTANGLE, { x, y, w: 1.9, h: 1.3, fill: { color: C.dark }, line: { color: C.dark } });
      txt(s, n, { x: x + 0.18, y: y + 0.12, w: 1.6, h: 0.6, fontSize: n.length > 3 ? 26 : 30, bold: true, color: C.gold, valign: 'middle' });
      txt(s, l, { x: x + 0.18, y: y + 0.72, w: 1.6, h: 0.5, fontSize: 11, color: C.white, valign: 'top' });
    });
    footer(s, false);
    s.addNotes(`[~1.5 min] Four heaters across the Carson and Wilmington sides of LAR. Coker #1 Heaters 1 and 2 four times a year each, Coker #2 Heater 3 three times, Wilmington DCU H-101 once. That is 12 decokes a year and 60 over the five-year term.
Commercial basis as submitted: lump sum per occurrence, mob/demob waived, 30-day terms. Stand-by not caused by USA DeBusk at the attached rates.
Key message: this is a program, not a one-off job, and we've planned it that way.
Point to the photo: "That's your coker at Carson, from Marathon's own site. It's the unit we'd be cleaning four times a year."`);
  }

  // =====================================================================
  // 4. METHODOLOGY — PROCESS
  {
    const s = pres.addSlide();
    bg(s, C.white);
    s.addImage({ path: IMG + 'slot_method.jpg', x: 9.33, y: 0, w: 4.0, h: H });
    chip(s, '01', 'Methodology', false);
    title(s, 'Bi-directional mechanical decoking', false, { w: 8.4 });
    sub(s, 'Every pass follows the same controlled sequence', false, { w: 8.4 });
    const steps = [
      ['Rig-in & pressure test', 'Connect 300# launchers and receivers; fill and test before any launch'],
      ['Baseline flow test', 'Record pressure at a set rate for a before-and-after comparison'],
      ['Gauge foam run', 'Proves the pass is open and sets the initial pig size'],
      ['Scraper pig progression', 'Carbide-studded pigs run in both directions, stepped up ⅛" per clean pass'],
      ['Oversize polish', 'Up to tube ID + ¼" maximum, with real-time pressure monitoring'],
      ['Gauge foam & sign-off', 'Line-size foam witnessed by Marathon, final flow test, pass signed clean'],
    ];
    const x0 = 0.6, y0 = 2.3, rowH = 0.73;
    s.addShape(pres.shapes.LINE, { x: x0 + 0.27, y: y0 + 0.27, w: 0, h: rowH * 5, line: { color: C.rule, width: 2 } });
    steps.forEach(([h, d], i) => {
      const y = y0 + i * rowH;
      s.addShape(pres.shapes.OVAL, { x: x0, y, w: 0.54, h: 0.54, fill: { color: i === 5 ? C.gold : C.dark }, line: { color: C.white, width: 2 } });
      txt(s, String(i + 1), { x: x0, y, w: 0.54, h: 0.54, fontSize: 15, bold: true, color: i === 5 ? C.dark : C.gold, align: 'center', valign: 'middle' });
      txt(s, h, { x: x0 + 0.8, y: y - 0.02, w: 7.7, h: 0.3, fontSize: 15, bold: true, color: C.text });
      txt(s, d, { x: x0 + 0.8, y: y + 0.28, w: 7.7, h: 0.3, fontSize: 12.5, color: C.muted });
    });
    footer(s, false);
    s.addNotes(`[~2.5 min] Walk the six steps. Emphasize "bi-directional": the TriMax reverses flow from the operator station without hose changes, so pigs work the coke from both sides. That is how we clear tight spots and plug headers.
Step 1: we fill and pressure-test the rig before anything launches.
Step 2: the baseline flow test gives an objective before/after comparison at the same rate and direction.
Step 4: pigs step up in 1/8" increments only after a clean pass at the current size. We never jump sizes on hard coke.
Step 5: the maximum oversize is capped at the smallest tube ID + 0.250". That protects the tube wall from grooving; over-cleaning is a real risk and we control it.
Step 6: Marathon witnesses the final gauge foam and signs off per pass (detail in topic 5).`);
  }

  // =====================================================================
  // 5. PIG PROGRESSION PLAN
  {
    const s = pres.addSlide();
    bg(s, C.white);
    chip(s, '01', 'Methodology', false);
    title(s, 'Pig progression plan by heater', false);
    sub(s, 'Answers RFI item SP-2; the gauge foam run sets the starting size, the tube ID sets the ceiling', false);
    const plans = [
      ['Carson Cokers, Heaters #1, #2, #3', 'Governing ID 3.826"  (4" Sch 80)', ['Gauge\nfoam', 'Initial', '+⅛"', '+⅛"', '+⅛"', '3.826"', '4.076"']],
      ['Wilmington DCU H-101', 'Tube ID 4.026"  (4.5" OD × 0.237")', ['Gauge\nfoam', 'Initial', '+⅛"', '+⅛"', '+⅛"', '4.026"', '4.276"']],
    ];
    const stageLbl = ['Run first', 'Set by foam', 'Step', 'Step', 'Step', 'Line size', 'Max'];
    plans.forEach(([name, idl, sizes], p) => {
      const top = 2.3 + p * 2.4;
      txt(s, name, { x: 0.6, y: top, w: 6, h: 0.35, fontSize: 16, bold: true, color: C.text });
      txt(s, idl, { x: 0.6, y: top + 0.35, w: 6, h: 0.3, fontSize: 12, color: C.muted });
      const baseY = top + 1.72, bw = 1.02, gap = 0.1;
      sizes.forEach((sz, i) => {
        const h = 0.42 + i * 0.11;
        const x = 0.6 + i * (bw + gap);
        const isMax = i === sizes.length - 1, isLine = i === sizes.length - 2;
        const fill = isMax ? C.gold : (i === 0 ? C.rule : C.dark);
        s.addShape(pres.shapes.RECTANGLE, { x, y: baseY - h, w: bw, h, fill: { color: fill }, line: { color: fill } });
        txt(s, sz, { x, y: baseY - h, w: bw, h, fontSize: 12.5, bold: true, color: isMax || i === 0 ? C.dark : C.white, align: 'center', valign: 'middle' });
        txt(s, stageLbl[i], { x, y: baseY + 0.05, w: bw, h: 0.25, fontSize: 10, color: isLine || isMax ? C.text : C.muted, bold: isLine || isMax, align: 'center' });
      });
    });
    // rule card
    s.addShape(pres.shapes.RECTANGLE, { x: 8.75, y: 2.35, w: 3.98, h: 4.5, fill: { color: C.dark }, line: { color: C.dark } });
    txt(s, 'The sizing rule', { x: 9.05, y: 2.6, w: 3.4, h: 0.4, fontSize: 16, bold: true, color: C.gold });
    txt(s, 'Max pig OD =\nsmallest tube ID + 0.250"', { x: 9.05, y: 3.05, w: 3.5, h: 0.7, fontSize: 16, bold: true, color: C.white, valign: 'top' });
    txt(s, [
      { text: 'Step up ⅛" after each clean pass', options: { bullet: true, breakLine: true } },
      { text: 'Pig wear drives size & appendages', options: { bullet: true, breakLine: true } },
      { text: 'Body length set for bends & mule ears', options: { bullet: true } },
    ], { x: 9.05, y: 3.8, w: 3.5, h: 0.95, fontSize: 12, color: C.soft, valign: 'top', paraSpaceAfter: 4 });
    s.addShape(pres.shapes.RECTANGLE, { x: 9.02, y: 4.83, w: 3.44, h: 3.4 * 437 / 900 + 0.04, fill: { color: C.char2 }, line: { color: C.char2 } });
    s.addImage({ path: IMG + 'pigs_lineup.jpg', x: 9.04, y: 4.85, w: 3.4, h: 3.4 * 437 / 900 });
    txt(s, 'Real pigs from a USA DeBusk job', { x: 9.04, y: 6.55, w: 3.4, h: 0.22, fontSize: 9, italic: true, color: C.soft });
    footer(s, false);
    s.addNotes(`[~2.5 min] RFI item SP-2 asked for a pig progression plan per heater. This is it.
The ceiling is fixed by our sizing rule: smallest tube ID plus a quarter inch. On the Carson cokers the governing ID is 3.826" (4" Sch 80), so the maximum is 4.076". On H-101 the ID is 4.026", so the maximum is 4.276".
The photo in the card is a real set from one of our jobs: foam, carbide-studded, then pigs showing wear.
We don't pick a starting size in advance. The first run is a gauge foam: how it comes out of the pass tells us how much the bore is restricted, and that sets the initial pig size. From there we step up 1/8" at a time, only after a clean pass at the current size, until we reach line size and then the maximum. Wear marks on a pig show where coke remains, and we change size and appendage type from that evidence.
If asked about short-radius bends or mule ears: pig body length and flexibility are selected for the bend geometry, not just the diameter.`);
  }

  // =====================================================================
  // 6. HEATER DATA & COIL CONTROLS
  {
    const s = pres.addSlide();
    bg(s, C.light);
    chip(s, '01', 'Methodology', false);
    title(s, 'Heater data & coil-specific controls', false);
    const hdr = (t) => ({ text: t, options: { bold: true, color: C.white, fill: { color: C.dark }, fontSize: 11.5 } });
    const data = [
      ['Carson Cokers', 'Convection', '2', "2,268'", '3.826"', 'SS 321'],
      ['Carson Cokers', 'Radiant', '2', "4,032'", '3.826" / 4.026"', 'A335 P9'],
      ['H-101', 'Convection', '4', "2,508'", '4.026"', 'A312 347H'],
      ['H-101', 'Radiant', '4', "7,524'", '4.026"', 'A312 347H'],
    ];
    const rows = [[hdr('Heater'), hdr('Section'), hdr('Passes'), hdr('Footage'), hdr('Tube ID'), hdr('Metallurgy')]]
      .concat(data.map((r, i) => r.map(c => ({ text: c, options: { fill: { color: i % 2 ? 'F7F7F7' : C.white }, color: C.text, fontSize: 12 } }))));
    s.addTable(rows, { x: 0.6, y: 1.95, w: 7.3, colW: [1.35, 1.25, 0.85, 1.05, 1.55, 1.25], rowH: 0.5, fontFace: FONT, border: { type: 'solid', pt: 0.75, color: C.rule }, valign: 'middle' });
    txt(s, 'Source: DSP#26098 Rev 1, Technical Data (coil data provided by Marathon)', { x: 0.6, y: 4.6, w: 7.3, h: 0.3, fontSize: 10, color: C.grey, italic: true });
    // big footage callouts under table
    const fz = [["6,300'", 'per Carson heater'], ["10,032'", 'on H-101'], ['Grade', 'launcher access (H-101 radiant: grade & 1st deck)']];
    fz.forEach(([n, l], i) => {
      const x = 0.6 + i * 2.5;
      txt(s, n, { x, y: 5.15, w: 2.3, h: 0.7, fontSize: 30, bold: true, color: C.text });
      txt(s, l, { x, y: 5.85, w: 2.3, h: 0.35, fontSize: 12, color: C.muted });
    });
    const cards = [
      ['FaTint', 'Stainless coils', 'Water quality verified before fill; passivation coordinated with Marathon; no galvanized contact with tubes'],
      ['FaLink', 'Connections', "600# RFWN coil flanges adapted to USA DeBusk 300# launchers and receivers"],
      ['FaSyncAlt', 'Return bends', 'Pig length and flexibility selected for 180° returns and mule ears'],
    ];
    for (let i = 0; i < cards.length; i++) {
      const [ic, h, d] = cards[i];
      const y = 1.95 + i * 1.6;
      s.addShape(pres.shapes.RECTANGLE, { x: 8.4, y, w: 4.33, h: 1.42, fill: { color: C.white }, line: { color: C.white }, shadow: shadow() });
      await iconCircle(s, ic, 8.62, y + 0.3, 0.72, C.dark, C.gold);
      txt(s, h, { x: 9.55, y: y + 0.2, w: 3.0, h: 0.35, fontSize: 15, bold: true, color: C.text });
      txt(s, d, { x: 9.55, y: y + 0.55, w: 3.05, h: 0.8, fontSize: 11.5, color: C.muted, valign: 'top' });
    }
    footer(s, false);
    s.addNotes(`[~1.5 min] Numbers here are exactly as submitted in the proposal's Technical Data page, from the coil data Marathon provided.
Per Carson heater: 1,134' per pass convection plus 2,016' per pass radiant, about 3,150' per pass and 6,300' per heater. H-101: 627' plus 1,881' per pass across 4 passes, about 10,000'.
Three coil-specific controls:
1) Stainless. The Carson convection and all of H-101 are stainless. We verify water quality before fill, coordinate with Marathon's passivation requirements, and keep galvanized hardware off the tubes.
2) Connections. The coils have 600# RFWN flanges and our launchers/receivers are 300#; Marathon supplies the inlet/outlet spools and adapters, per the proposal's provided-items list.
3) Bends. 180° returns and mule ears set pig length and flexibility, not just diameter.
Launcher connections are at grade (process control valves / radiant outlets); the H-101 radiant outlets are at grade and the 1st deck.`);
  }

  // =====================================================================
  // 7. EXECUTION PLAN — GANTT
  {
    const s = pres.addSlide();
    bg(s, C.white);
    chip(s, '02', 'Execution plan & schedule', false);
    title(s, 'Execution plan per occurrence', false);
    sub(s, 'Continuous 24/7 pigging on 12-hour shifts; passes pigged in conjunction', false);
    const rows = [
      ['Carson Coker #1, Heater #1', [['Rig-in', 6], ['Pig all coils in conjunction', 34], ['Rig-out', 6]]],
      ['Carson Coker #1, Heater #2', [['Rig-in', 6], ['Pig all coils in conjunction', 34], ['Rig-out', 6]]],
      ['Carson Coker #2, Heater #3', [['Rig-in', 6], ['Pig all coils in conjunction', 34], ['Rig-out', 6]]],
      ['Wilmington DCU, H-101', [['Rig-in', 6], ['Pig coils 1 & 2', 18], ['Rig-over', 4], ['Pig coils 3 & 4', 18], ['Rig-out', 6]]],
    ];
    const lx = 0.6, gx = 3.75, gw = 7.9, maxH = 52, sc = gw / maxH, top = 2.55, rh = 0.62, rg = 0.34;
    // hour grid
    for (let hr = 0; hr <= 48; hr += 12) {
      const x = gx + hr * sc;
      s.addShape(pres.shapes.LINE, { x, y: top - 0.15, w: 0, h: rows.length * (rh + rg), line: { color: 'E6E6E6', width: 1, dashType: 'dash' } });
      txt(s, `${hr} h`, { x: x - 0.4, y: top - 0.5, w: 0.8, h: 0.28, fontSize: 10, color: C.grey, align: 'center' });
    }
    rows.forEach(([name, segs], r) => {
      const y = top + r * (rh + rg);
      txt(s, name, { x: lx, y, w: 3.0, h: rh, fontSize: 13, bold: true, color: C.text, valign: 'middle' });
      let t = 0;
      segs.forEach(([lbl, hrs]) => {
        const pig = lbl.startsWith('Pig');
        const fill = pig ? C.gold : (lbl === 'Rig-over' ? C.soft : C.dark);
        const x = gx + t * sc, w = hrs * sc;
        s.addShape(pres.shapes.RECTANGLE, { x, y, w: w - 0.03, h: rh, fill: { color: fill }, line: { color: fill } });
        const show = pig ? `${lbl}: ${hrs} h` : `${hrs}`;
        txt(s, show, { x, y, w: w - 0.03, h: rh, fontSize: pig ? 12 : 12, bold: true, color: pig || lbl === 'Rig-over' ? C.dark : C.white, align: 'center', valign: 'middle' });
        t += hrs;
      });
      txt(s, `${t} h`, { x: gx + t * sc + 0.12, y, w: 0.9, h: rh, fontSize: 18, bold: true, color: C.text, valign: 'middle' });
    });
    // legend
    const lg = [[C.dark, 'Rig-in / rig-out'], [C.gold, 'Pigging'], [C.soft, 'Rig-over']];
    lg.forEach(([c, l], i) => {
      const x = 3.75 + i * 2.3;
      s.addShape(pres.shapes.RECTANGLE, { x, y: 6.45, w: 0.28, h: 0.2, fill: { color: c }, line: { color: c } });
      txt(s, l, { x: x + 0.38, y: 6.4, w: 1.9, h: 0.3, fontSize: 11, color: C.muted });
    });
    txt(s, 'Per occurrence; durations are not consecutive', { x: 0.6, y: 6.4, w: 3.0, h: 0.4, fontSize: 10, italic: true, color: C.grey, valign: 'top' });
    footer(s, false);
    s.addNotes(`[~2.5 min] Each occurrence as quoted:
Carson heaters: 6 hours rig-in, 34 hours pigging all coils in conjunction, 6 hours rig-out: 46 hours total.
H-101: 6 rig-in, 18 hours on coils 1 and 2 together, a 4-hour rig-over to coils 3 and 4, 18 hours, 6 rig-out: 52 hours.
"In conjunction" means both Carson passes are pigged at the same time, each on its own pump and operator station, so elapsed time is one coil's time, not two. On a 2-pass heater the TriMax's third pump is a spare: if a pump goes down, the job keeps running.
We run 24/7 on 12-hour day/night shifts, so a Carson heater is back in Marathon's hands in about two days.
Durations come from footage and our historical performance. Actual hardness and thickness of deposits can move them, and the proposal covers that.`);
  }

  // =====================================================================
  // 8. FIVE-YEAR PROGRAM
  {
    const s = pres.addSlide();
    bg(s, C.dark);
    chip(s, '02', 'Execution plan & schedule', true);
    title(s, 'Five-year program at a glance', true);
    sub(s, "Illustrative annual cadence: dates are set to Marathon's run-length and turnaround plan", true);
    const hs = [['Coker #1, Heater #1', 4], ['Coker #1, Heater #2', 4], ['Coker #2, Heater #3', 3], ['DCU, H-101', 1]];
    const months = ['J', 'F', 'M', 'A', 'M', 'J', 'J', 'A', 'S', 'O', 'N', 'D'];
    const gx = 3.4, cw = 0.42;
    months.forEach((m, i) => txt(s, m, { x: gx + i * cw, y: 2.3, w: cw, h: 0.3, fontSize: 11, color: C.grey, align: 'center' }));
    const slots = { 4: [1, 4, 7, 10], 3: [2, 6, 10], 1: [8] };
    const offs = [0, 1, 0, 0];
    hs.forEach(([n, f], r) => {
      const y = 2.75 + r * 0.8;
      txt(s, n, { x: 0.6, y, w: 2.7, h: 0.5, fontSize: 13, bold: true, color: C.white, valign: 'middle' });
      s.addShape(pres.shapes.RECTANGLE, { x: gx, y: y + 0.08, w: cw * 12, h: 0.34, fill: { color: C.char }, line: { color: C.char } });
      slots[f].forEach(m => {
        const mm = (m + offs[r]) % 12;
        s.addShape(pres.shapes.OVAL, { x: gx + mm * cw + (cw - 0.4) / 2, y: y + 0.05, w: 0.4, h: 0.4, fill: { color: C.gold }, line: { color: C.dark, width: 2 } });
      });
      txt(s, `${f}× / yr`, { x: gx + cw * 12 + 0.25, y, w: 1.0, h: 0.5, fontSize: 13, color: C.soft, valign: 'middle' });
    });
    const st = [['12', 'decokes a year'], ['60', 'decokes in 5 years'], ['2,790', 'project hours'], ['$0', 'mob / demob']];
    st.forEach(([n, l], i) => {
      const y = 2.2 + i * 1.12;
      s.addShape(pres.shapes.RECTANGLE, { x: 10.0, y, w: 2.73, h: 0.98, fill: { color: C.char }, line: { color: C.char } });
      txt(s, n, { x: 10.2, y: y + 0.08, w: 1.3, h: 0.8, fontSize: 28, bold: true, color: C.gold, valign: 'middle' });
      txt(s, l, { x: 11.45, y: y + 0.08, w: 1.2, h: 0.8, fontSize: 11.5, color: C.white, valign: 'middle' });
    });
    txt(s, 'Same crew leadership, same equipment and same procedures every visit: each decoke builds on the last one\'s records.', { x: 0.6, y: 6.1, w: 8.9, h: 0.6, fontSize: 14, italic: true, color: C.soft, valign: 'top' });
    footer(s, true);
    s.addNotes(`[~1.5 min] The dots show one year of the program; exact dates follow Marathon's run-length and turnaround plan, not ours.
12 decokes a year, 60 over the term, 2,790 project hours, and mobilization/demobilization waived because LAR is serviced as a program.
The real value of a recurring program: each decoke on the same heater builds on the last. We keep heater-specific records of pig sizes, hours and problem spots, so every visit starts smarter than the last.`);
  }

  // =====================================================================
  // 9. OPERATIONAL READINESS & RESOURCES
  {
    const s = pres.addSlide();
    bg(s, C.white);
    s.addImage({ path: IMG + 'slot_ready.jpg', x: 0, y: 0, w: 4.6, h: H });
    const X = 5.1;
    chip(s, '03', 'Readiness & resources', false, X);
    title(s, 'Crew & equipment, every occurrence', false, { x: X, w: 7.6, fontSize: 30 });
    const col = (x, head, ic, items) => {
      txt(s, head, { x: x + 0.6, y: 2.0, w: 3.0, h: 0.4, fontSize: 16, bold: true, color: C.text, valign: 'middle' });
      items.forEach(([n, l], i) => {
        const y = 2.65 + i * 0.72;
        txt(s, n, { x, y, w: 0.55, h: 0.55, fontSize: 22, bold: true, color: C.gold, valign: 'middle' });
        txt(s, l, { x: x + 0.6, y, w: 3.0, h: 0.55, fontSize: 13, color: C.text, valign: 'middle' });
      });
    };
    col(X, 'Equipment', 'FaTruck', [['1', 'TriMax triple pumper'], ['1', 'Support unit: fittings, tooling, spares'], ['2', 'Crew trucks']]);
    col(X + 3.85, 'Manpower', 'FaUsers', [['2', 'Supervisors: 1 day, 1 night'], ['3', 'Operators: 2 day, 1 night'], ['1', 'Project manager']]);
    await iconCircle(s, 'FaTruck', X, 1.95, 0.48, C.dark, C.gold);
    await iconCircle(s, 'FaUsers', X + 3.85, 1.95, 0.48, C.dark, C.gold);
    const st = [['~5%', 'crew turnover, last 12 months'], ['24/7', 'two 12-hour shifts'], ['100%', 'training verified before mobilization']];
    st.forEach(([n, l], i) => {
      const x = X + i * 2.55;
      s.addShape(pres.shapes.RECTANGLE, { x, y: 5.05, w: 2.35, h: 1.55, fill: { color: C.dark }, line: { color: C.dark } });
      txt(s, n, { x: x + 0.2, y: 5.2, w: 2.0, h: 0.7, fontSize: 30, bold: true, color: C.gold });
      txt(s, l, { x: x + 0.2, y: 5.9, w: 2.0, h: 0.6, fontSize: 11.5, color: C.white, valign: 'top' });
    });
    footer(s, false, X);
    s.addNotes(`[~2 min] Every occurrence gets the same package: one TriMax, one support unit carrying fittings, tooling and spares, two crew trucks.
Crew: day shift is a supervisor and two operators; night shift is a supervisor and an operator; Travis Trenholm manages the project.
Readiness: turnover has run about 5% over the last 12 months. We hold onto people with competitive pay, ongoing training and certification, career paths, and dedicated core crews per site. For LAR that means the same faces on the same heaters.
Every technician is USA DeBusk-certified, selected by heater-type experience, with training verified before mobilization. The personnel training documents (SSHASP) were attached to the RFI.`);
  }

  // =====================================================================
  // 10. PROJECT TEAM ORG CHART
  {
    const s = pres.addSlide();
    bg(s, C.dark);
    chip(s, '03', 'Readiness & resources', true);
    title(s, 'Your LAR project team', true);
    const box = (x, y, w, name, role, gold) => {
      s.addShape(pres.shapes.RECTANGLE, { x, y, w, h: 0.95, fill: { color: gold ? C.gold : C.char }, line: { color: gold ? C.gold : C.char2 } });
      txt(s, name, { x: x + 0.2, y: y + 0.12, w: w - 0.4, h: 0.38, fontSize: 16, bold: true, color: gold ? C.dark : C.white });
      txt(s, role, { x: x + 0.2, y: y + 0.5, w: w - 0.4, h: 0.35, fontSize: 12, color: gold ? C.dark : C.soft });
    };
    const ln = (x, y, w, h, dash) => s.addShape(pres.shapes.LINE, { x, y, w, h, line: { color: C.grey, width: 1.5, dashType: dash ? 'dash' : 'solid' } });
    const cx = 6.67, bw = 3.6;
    box(cx - bw / 2, 1.9, bw, 'Anthony Fazio', 'VP Operations');
    ln(cx, 2.85, 0, 0.45);
    box(cx - bw / 2, 3.3, bw, 'Marshall Douglas', 'Director of Pigging Operations', true);
    ln(cx + bw / 2, 3.78, 1.0, 0, true);
    box(cx + bw / 2 + 1.0, 3.3, 3.2, 'Jason Harman', 'Commercial Manager');
    ln(cx, 4.25, 0, 0.45);
    box(cx - bw / 2, 4.7, bw, 'Travis Trenholm', 'Pigging Operations Manager (PM)');
    ln(cx, 5.65, 0, 0.3);
    ln(cx - 2.2, 5.95, 4.4, 0);
    ln(cx - 2.2, 5.95, 0, 0.2); ln(cx + 2.2, 5.95, 0, 0.2);
    const crew = (x, t, d) => {
      s.addShape(pres.shapes.RECTANGLE, { x, y: 6.15, w: 3.2, h: 0.72, fill: { color: C.char }, line: { color: C.char2 } });
      txt(s, t, { x: x + 0.15, y: 6.18, w: 2.9, h: 0.33, fontSize: 13, bold: true, color: C.gold });
      txt(s, d, { x: x + 0.15, y: 6.5, w: 2.9, h: 0.3, fontSize: 11, color: C.soft });
    };
    crew(cx - 2.2 - 1.6, 'Day shift', '1 supervisor, 2 operators');
    crew(cx + 2.2 - 1.6, 'Night shift', '1 supervisor, 1 operator');
    txt(s, 'Site org chart finalized at award', { x: 0.6, y: 6.45, w: 2.5, h: 0.3, fontSize: 10, italic: true, color: C.grey });
    footer(s, true);
    s.addNotes(`[~1 min] Leadership line: Anthony Fazio, VP Operations; me as Director of Pigging Operations; Travis Trenholm as the project manager on every LAR occurrence. Jason Harman is the commercial point of contact.
One point of contact manages work flow and daily updates to Marathon.
Leadership resumes were included with the RFI response; the full site org chart is issued at award.`);
  }

  // =====================================================================
  // 11. TRIMAX
  {
    const s = pres.addSlide();
    bg(s, C.dark);
    s.addImage({ path: IMG + 'slot_trimax.jpg', x: 0, y: 0, w: W, h: H });
    s.addImage({ path: IMG + 'fade_left.png', x: 0, y: 0, w: W, h: H });
    s.addImage({ path: IMG + 'fade_left.png', x: 0, y: 0, w: 10.5, h: H });
    chip(s, '04', 'Equipment & technology', true);
    title(s, 'The TriMax triple pumper', true, { w: 7 });
    const specs = [
      ['FaCogs', 'Three independent pump systems', 'Closed-loop, bi-directional; 50% more productive than a twin pumper'],
      ['FaDesktop', 'Automated HMI control', 'Three 17" touchscreens, automated digital pig logs'],
      ['FaTachometerAlt', '150–300 psi working pressure', 'Pump rated 600 psi; 500–550 psi effective after valve losses'],
      ['FaChartLine', 'Real-time sensor data', 'Coke shows as pressure spikes at the operator interface'],
      ['FaLeaf', 'Cummins QSL9, 333 bhp, Tier 4 Final', 'CARB-registered engines, California-ready'],
    ];
    for (let i = 0; i < specs.length; i++) {
      const [ic, h, d] = specs[i];
      const y = 1.95 + i * 0.83;
      await iconCircle(s, ic, 0.6, y, 0.62, C.gold, C.dark);
      txt(s, h, { x: 1.4, y: y - 0.02, w: 5.6, h: 0.35, fontSize: 16, bold: true, color: C.white });
      txt(s, d, { x: 1.4, y: y + 0.32, w: 5.6, h: 0.3, fontSize: 12, color: C.soft });
    }
    // pressure envelope bar
    {
      const bx = 0.6, bw = 6.3, by = 6.45, bh = 0.18, sc = bw / 600;
      txt(s, 'OPERATING PRESSURE, PSI', { x: bx, y: by - 0.42, w: 4, h: 0.22, fontSize: 9.5, bold: true, color: C.soft, charSpacing: 1 });
      s.addShape(pres.shapes.RECTANGLE, { x: bx, y: by, w: bw, h: bh, fill: { color: '3A3A3A' }, line: { color: '3A3A3A' } });
      s.addShape(pres.shapes.RECTANGLE, { x: bx + 150 * sc, y: by, w: 150 * sc, h: bh, fill: { color: C.gold }, line: { color: C.gold } });
      s.addShape(pres.shapes.RECTANGLE, { x: bx + 500 * sc, y: by, w: 50 * sc, h: bh, fill: { color: 'B8860B' }, line: { color: 'B8860B' } });
      s.addShape(pres.shapes.LINE, { x: bx + bw, y: by - 0.08, w: 0, h: bh + 0.16, line: { color: C.white, width: 1.5 } });
      [0, 150, 300, 500, 600].forEach(v => txt(s, String(v), { x: bx + v * sc - 0.3, y: by + bh + 0.04, w: 0.6, h: 0.2, fontSize: 9, color: C.soft, align: 'center' }));
      txt(s, 'Normal pigging', { x: bx + 150 * sc, y: by - 0.24, w: 150 * sc, h: 0.2, fontSize: 9.5, bold: true, color: C.gold, align: 'center' });
      txt(s, 'Effective max', { x: bx + 440 * sc, y: by - 0.24, w: 170 * sc, h: 0.2, fontSize: 9.5, bold: true, color: 'E0B000', align: 'center' });
    }
    footer(s, true);
    s.addNotes(`[~2 min] This is the core of our service. Three independent pump assemblies in one trailer, each with its own operator station, so three passes can run at the same time. At LAR we pig both Carson passes together and H-101 in pairs, which leaves the third pump as an on-board spare. Against a dual unit the triple raises productivity by about 50%, and on a two-pass Carson heater the third pump is 100% spare capacity: if one pump goes down, the job doesn't stop.
The spare pump can also propel a smart pig, so inspection runs don't need extra equipment.
Each operator station has a 17" automated HMI touchscreen, and pig logs are recorded digitally (next slide).
Other features built into the unit: temperature-controlled pig compartments so the pigs keep their cleaning characteristics, antifoam injection, a coke transfer chute, and guided-radar tank level indicators. On-board tankage is 3,000 gal clean and 2,000 gal return.
The bar at the bottom is our operating window: normal pigging runs 150 to 300 psi. The pump is rated to 600 psi, but after losses through our valves the realistic ceiling at the pig is 500 to 550, and above 500 the crew works an over-pressure checklist. The manufacturer's pump curves are in the appendix if anyone wants them.
Real-time sensor data feeds the operator interface, where coke shows up as a pressure spike. The technician can stop and scrub that exact spot. Flow direction reverses from the station without hose changes.
Power is a Cummins QSL9 at 333 bhp, Tier 4, CARB-registered. California compliance is two slides on, after the operator screen.`);
  }

  // =====================================================================
  // 11b. HMI / PIGGING SOFTWARE
  {
    const s = pres.addSlide();
    bg(s, C.dark);
    chip(s, '04', 'Equipment & technology', true);
    title(s, 'Real-time control at every operator station', true);
    const ix = 0.6, iy = 1.9, iw = 6.6, ih = 6.6 * 1200 / 1600;
    s.addShape(pres.shapes.RECTANGLE, { x: ix - 0.08, y: iy - 0.08, w: iw + 0.16, h: ih + 0.16, fill: { color: C.char2 }, line: { color: C.char2 } });
    s.addImage({ path: IMG + 'hmi2.jpg', x: ix, y: iy, w: iw, h: ih });
    const marks = [[0.09, 0.70], [0.515, 0.578], [0.20, 0.28], [0.37, 0.07], [0.36, 0.24], [0.793, 0.09]];
    marks.forEach(([fx, fy], i) => {
      const d = 0.4, x = ix + fx * iw - d / 2, y = iy + fy * ih - d / 2;
      s.addShape(pres.shapes.OVAL, { x, y, w: d, h: d, fill: { color: C.gold }, line: { color: C.dark, width: 2 } });
      txt(s, String(i + 1), { x, y, w: d, h: d, fontSize: 13, bold: true, color: C.dark, align: 'center', valign: 'middle' });
    });
    const items = [
      ['Live trends', 'Pressure ahead of and behind the pig, plus flow; coke shows as a spike'],
      ['Flow & pressure', 'GPM and psi at the pump, updated continuously'],
      ['Tank levels', 'Clean and effluent tanks on guided-radar indicators'],
      ['Setpoint alarms', 'Upper and lower limits on pressure and flow trigger alerts'],
      ['Digital pig logs', 'Pass completion, pig run sheet and data sheet recorded automatically'],
      ['One station per pass', 'Left, center and right stations run independently'],
    ];
    items.forEach(([h, d], i) => {
      const y = 1.9 + i * 0.8;
      s.addShape(pres.shapes.OVAL, { x: 7.95, y: y + 0.03, w: 0.4, h: 0.4, fill: { color: C.gold }, line: { color: C.gold } });
      txt(s, String(i + 1), { x: 7.95, y: y + 0.03, w: 0.4, h: 0.4, fontSize: 13, bold: true, color: C.dark, align: 'center', valign: 'middle' });
      txt(s, h, { x: 8.55, y: y - 0.02, w: 4.2, h: 0.3, fontSize: 14, bold: true, color: C.white });
      txt(s, d, { x: 8.55, y: y + 0.28, w: 4.2, h: 0.45, fontSize: 11.5, color: C.soft, valign: 'top' });
    });
    footer(s, true);
    s.addNotes(`[~1.5 min] This is the operator screen from a TriMax station, the same software every LAR pass runs on.
Walk the numbers: (1) the trend at the bottom plots pressure ahead of the pig, pressure behind it, and flow rate. When the pig meets coke you see the spike, and that's the "sensor data" indicator in our cleanliness verification. (2) Live GPM and psi. (3) Clean and effluent tank levels from guided-radar indicators. (4) Setpoint alarms; this one shows a clean-tank-low alert. (5) Pass completion and the pig run sheet and data sheet, so the pig log builds itself. (6) Each pass has its own station: left, center, right.
The takeaway for Marathon: every decision on a pass is made from live data, and the record is automatic.`);
  }

  // =====================================================================
  // 12. CALIFORNIA-READY FLEET
  {
    const s = pres.addSlide();
    bg(s, C.white);
    chip(s, '04', 'Equipment & technology', false);
    title(s, 'California-ready, CARB-registered fleet', false);
    sub(s, 'CARB Statewide Portable Equipment Registration (PERP); certificates shown', false);
    const st = [['6', 'SCAQMD-ready triple-pass units'], ['18', 'registered pumping engines'], ['Tier 4', 'engines (blue placard)'], ['0.015', 'g/bhp-hr diesel PM emission factor']];
    st.forEach(([n, l], i) => {
      const x = 0.6 + (i % 2) * 3.35, y = 2.3 + Math.floor(i / 2) * 1.55;
      txt(s, n, { x, y, w: 3.1, h: 0.8, fontSize: 40, bold: true, color: C.text });
      txt(s, l, { x, y: y + 0.8, w: 3.1, h: 0.4, fontSize: 13, color: C.muted });
    });
    // certs fanned
    const certs = [['cert_t1.png', 'TriMax 1'], ['cert_t2.png', 'TriMax 2'], ['cert_t6.png', 'TriMax 6']];
    certs.forEach(([f, l], i) => {
      const x = 7.35 + i * 1.85, y = 2.1;
      s.addImage({ path: IMG + f, x, y, w: 1.7, h: 2.21, shadow: shadow() });
      txt(s, l, { x, y: y + 2.3, w: 1.7, h: 0.3, fontSize: 11, bold: true, color: C.text, align: 'center' });
    });
    txt(s, 'CARB PERP registration certificates', { x: 7.35, y: 4.95, w: 5.4, h: 0.3, fontSize: 10, italic: true, color: C.grey, align: 'center' });
    // ancillaries
    s.addShape(pres.shapes.RECTANGLE, { x: 0.6, y: 5.45, w: 12.13, h: 1.3, fill: { color: C.light }, line: { color: C.light } });
    const anc = [['FaTools', 'Support unit'], ['FaLink', '300# launchers & receivers'], ['FaCheckCircle', 'Tested & certified hard and flex pipe'], ['FaBullseye', 'All pigs & foam swabs'], ['FaFilter', 'Optional: closed-loop filtration']];
    for (let i = 0; i < anc.length; i++) {
      const [ic, l] = anc[i];
      const x = 0.85 + i * 2.4;
      await iconCircle(s, ic, x, 5.73, 0.72, C.dark, C.gold);
      txt(s, l, { x: x + 0.82, y: 5.68, w: 1.38, h: 0.82, fontSize: 11.5, color: C.text, valign: 'middle' });
    }
    footer(s, false);
    s.addNotes(`[~1.5 min] California compliance is a gate for LAR, and we've cleared it. Every TriMax engine carries a CARB Statewide Portable Equipment Registration: certified Cummins QSL9 engines, Tier 4 blue placard, a diesel particulate emission factor of 0.015 g/bhp-hr. Six triple-pass units and 18 engines are registered for SCAQMD work, so no rental or swap-in equipment is needed to work in the Basin.
Everything needed arrives with the rig: support unit, 300# launchers and receivers, tested and certified hard and flex pipe connecting our equipment, all pigs and foam swabs. Closed-loop filtration is optional at the proposal rate: it runs continuously, captures coke fines from the effluent, and recycles clean water. That can save thousands of gallons of water a shift.`);
  }

  // =====================================================================
  // 13. 4-POINT VERIFICATION
  {
    const s = pres.addSlide();
    bg(s, C.dark);
    chip(s, '05', 'Cleanliness verification & QA/QC', true);
    title(s, 'Verifying every pass is clean', true);
    sub(s, 'Four independent indicators, reviewed side by side with Marathon', true);
    const cx = 6.67, cy = 4.55;
    s.addShape(pres.shapes.OVAL, { x: cx - 1.25, y: cy - 1.25, w: 2.5, h: 2.5, fill: { color: C.gold }, line: { color: C.gold } });
    txt(s, 'Joint\nsign-off\nper pass', { x: cx - 1.1, y: cy - 0.8, w: 2.2, h: 1.6, fontSize: 19, bold: true, color: C.dark, align: 'center', valign: 'middle' });
    const nodes = [
      ['FaChartLine', '1  Sensor data', 'Coke shows as a pressure spike; the tech stops and scrubs that exact spot', 0.6, 2.35, 'r'],
      ['FaWater', '2  Effluent returns', '"Black" in the return stream fades to nothing as the pass cleans', 8.95, 2.35, 'l'],
      ['PIGS', '3  Pig condition', 'Wear marks guide pig size and appendage choices', 0.6, 5.0, 'r'],
      ['FaCheckCircle', '4  Final gauge foam', 'Soft line-size (or slightly over) foam, witnessed by the Marathon rep', 8.95, 5.0, 'l'],
    ];
    for (const [ic, h, d, x, y] of nodes) {
      s.addShape(pres.shapes.RECTANGLE, { x, y, w: 3.78, h: 1.55, fill: { color: C.char }, line: { color: C.char2 } });
      if (ic === 'PIGS') {
        s.addImage({ path: IMG + 'pigs_three.jpg', x: x + 0.18, y: y + 0.4, w: 1.2, h: 1.2 * 441 / 720 });
        txt(s, h, { x: x + 1.5, y: y + 0.22, w: 2.2, h: 0.35, fontSize: 15, bold: true, color: C.white });
        txt(s, d, { x: x + 1.5, y: y + 0.6, w: 2.2, h: 0.85, fontSize: 11, color: C.soft, valign: 'top' });
        continue;
      }
      await iconCircle(s, ic, x + 0.22, y + 0.25, 0.62, C.gold, C.dark);
      txt(s, h, { x: x + 1.0, y: y + 0.22, w: 2.65, h: 0.35, fontSize: 15, bold: true, color: C.white });
      txt(s, d, { x: x + 1.0, y: y + 0.6, w: 2.65, h: 0.85, fontSize: 11.5, color: C.soft, valign: 'top' });
    }
    // connectors
    const ln = (x1, y1, x2, y2) => s.addShape(pres.shapes.LINE, { x: Math.min(x1, x2), y: Math.min(y1, y2), w: Math.abs(x2 - x1), h: Math.abs(y2 - y1), line: { color: C.gold, width: 1.5, dashType: 'dash' }, flipH: (x2 < x1) !== (y2 < y1) });
    ln(4.38, 3.1, cx - 0.95, cy - 0.8); ln(8.95, 3.1, cx + 0.95, cy - 0.8);
    ln(4.38, 5.8, cx - 0.95, cy + 0.8); ln(8.95, 5.8, cx + 0.95, cy + 0.8);
    txt(s, 'Proven in the field: successful sign-offs from all of our clients, and highly effective for first-attempt smart pig data.', { x: 0.6, y: 6.6, w: 12.1, h: 0.35, fontSize: 12, italic: true, color: C.gold, align: 'center' });
    s.addNotes(`[~2.5 min] How do we know a pass is clean? Four independent indicators, and the pass isn't called clean until all four agree.
1) Sensor data: live pressure data at the operator interface. Coke shows as a spike, and the technician can stop the pig and scrub that exact area.
2) Effluent: the technician watches the returns. The "black" (coke fines) in the stream fades to an unnoticeable amount as the pass cleans.
3) Pig condition: bi-directional runs leave tracking marks on the pigs (the photo shows real pigs after runs, with the wear visible). Those marks drive our size and appendage changes toward 100% removal.
4) Final gauge foam: when the interface, the water and the pigs all read clean, our shift leader invites the Marathon rep to watch the final gauge foam run. It's line size or slightly over and soft enough to mark, groove or deform on any remaining coke. Marathon reviews it with us and signs the pass off.
This is also why smart pig inspections after our cleans usually get good data on the first attempt.`);
    footer(s, true);
  }

  // =====================================================================
  // 14. QA/QC & DOCUMENTATION
  {
    const s = pres.addSlide();
    bg(s, C.light);
    chip(s, '05', 'Cleanliness verification & QA/QC', false);
    title(s, 'QA/QC from walkdown to job book', false);
    sub(s, 'Governed by the USA DeBusk QA/QC manual, submitted with the RFI response', false);
    const cols = [
      ['FaClipboardList', 'Before', ['Pre-job walkdown with operations', 'Coil data checked against Marathon records', 'JSA, permits and isolation confirmed', 'Pig progression staged by heater']],
      ['FaCogs', 'During', ['Daily report to one point of contact', 'Automated digital pig log per pass', 'Flow tests before and after at the same rate', 'JSA reviewed at every shift change']],
      ['FaBook', 'Close-out', ['Per-pass cleanliness sign-off', 'Final pig size recorded per pass', 'Job book delivered to Marathon', 'Post-job review and lessons learned']],
    ];
    for (let i = 0; i < cols.length; i++) {
      const [ic, h, items] = cols[i];
      const x = 0.6 + i * 4.1;
      s.addShape(pres.shapes.RECTANGLE, { x, y: 2.3, w: 3.9, h: 3.75, fill: { color: C.white }, line: { color: C.white }, shadow: shadow() });
      await iconCircle(s, ic, x + 0.3, 2.55, 0.75, C.dark, C.gold);
      txt(s, h, { x: x + 1.2, y: 2.62, w: 2.5, h: 0.6, fontSize: 22, bold: true, color: C.text, valign: 'middle' });
      txt(s, items.map((t, k) => ({ text: t, options: { bullet: { indent: 14 }, breakLine: k < items.length - 1 } })),
        { x: x + 0.3, y: 3.6, w: 3.35, h: 2.9, fontSize: 13, color: C.text, valign: 'top', paraSpaceAfter: 12 });
    }
    footer(s, false);
    s.addNotes(`[~1.5 min] QA/QC runs through the whole job, not just the end.
Before: walkdown, coil data check, JSA/permits/isolation, pig progression staged by heater.
During: work is documented in the job book with daily reports, pig logs and JSAs. One point of contact manages the work flow and daily updates to Marathon. Flow tests before and after at the same rate give an objective comparison.
Close-out: per-pass sign-off, final pig size recorded for each pass, the job book, and a post-job review. On a recurring program, that record is what makes the next decoke on the same heater faster.
The full QA/QC manual was attached to the RFI response.`);
  }

  // =====================================================================
  // 15. EMERGENCY RESPONSE
  {
    const s = pres.addSlide();
    bg(s, C.dark);
    s.addImage({ path: IMG + 'slot_shop.jpg', x: 0, y: 0, w: W, h: H });
    s.addShape(pres.shapes.RECTANGLE, { x: 0, y: 0, w: W, h: 2.1, fill: { color: '111111', transparency: 25 }, line: { color: '111111', transparency: 100 } });
    s.addImage({ path: IMG + 'fade_bottom_light.png', x: 0, y: 0, w: W, h: H });
    chip(s, '06', 'Emergency response & local resources', true);
    title(s, 'Ready when LAR needs us', true);
    sub(s, 'Shops, equipment and crews in Southern California / LA Basin, with regional support', true);
    const st = [['24/7', 'Dispatch and account manager, any hour'], ['Same day', 'Response for local needs'], ['< 24 hrs', 'Manpower & equipment anywhere else, from regional shops']];
    st.forEach(([n, l], i) => {
      const x = 0.6 + i * 4.1, y = 5.55;
      s.addShape(pres.shapes.RECTANGLE, { x, y, w: 3.9, h: 1.2, fill: { color: '151515', transparency: 15 }, line: { color: C.gold, width: 1.5 } });
      txt(s, n, { x: x + 0.2, y, w: 1.75, h: 1.2, fontSize: n.length > 5 ? 22 : 28, bold: true, color: C.gold, valign: 'middle' });
      txt(s, l, { x: x + 1.95, y, w: 1.85, h: 1.2, fontSize: 11.5, color: C.white, valign: 'middle' });
    });
    footer(s, true);
    s.addNotes(`[~2 min] Topic 6: emergency response and local resources.
We maintain shops, equipment and crews in the Southern California / LA Basin area with regional support. That local footprint allows same-day to next-day mobilization to LAR.
Support is 24/7: dispatch and the account manager can be reached at any hour, with on-call supervisors and crews for nights, weekends and holidays.
Response: same day for local needs, within 24 hours otherwise, with manpower and pigging/decoking equipment staged from our regional shops.
On the recurring program, the same crew that knows these heaters is the crew that answers an unplanned call.\nThe photo: a TriMax and its support unit staged in the shop, fueled and ready to roll.`);
  }

  // =====================================================================
  // 16. SAFETY PERFORMANCE
  {
    const s = pres.addSlide();
    bg(s, C.dark);
    chip(s, '07', 'Safety & risk mitigation', true);
    title(s, 'Safety performance', true);
    sub(s, 'Experience Modification Rate: 1.0 is the industry baseline; lower is better', true);
    s.addChart(pres.charts.BAR, [{ name: 'EMR', labels: ['2024', '2025', '2026'], values: [0.95, 0.62, 0.48] }], {
      x: 0.6, y: 2.2, w: 6.8, h: 4.5, barDir: 'col', barGapWidthPct: 55,
      chartColors: ['8A8A8A', 'C9A00A', C.gold], varyColors: true,
      showValue: true, dataLabelPosition: 'outEnd', dataLabelColor: C.white, dataLabelFontSize: 20, dataLabelFontBold: true, dataLabelFormatCode: '0.00',
      catAxisLabelColor: C.soft, catAxisLabelFontSize: 14, catAxisLineShow: false,
      valAxisHidden: true, valAxisMinVal: 0, valAxisMaxVal: 1.1, valGridLine: { style: 'none' }, catGridLine: { style: 'none' },
      showLegend: false, plotArea: { fill: { color: C.dark } }, chartArea: { fill: { color: C.dark } },
    });
    const tiles = [['A', 'ISNetworld safety grade'], ['0.48', 'EMR, 2026'], ['−49%', 'EMR since 2024'], ['0', 'fatalities in 3 years']];
    tiles.forEach(([n, l], i) => {
      const x = 7.9 + (i % 2) * 2.45, y = 2.3 + Math.floor(i / 2) * 2.2;
      s.addShape(pres.shapes.RECTANGLE, { x, y, w: 2.25, h: 2.0, fill: { color: C.char }, line: { color: C.char } });
      txt(s, n, { x: x + 0.2, y: y + 0.25, w: 1.9, h: 0.9, fontSize: 40, bold: true, color: C.gold });
      txt(s, l, { x: x + 0.2, y: y + 1.2, w: 1.9, h: 0.65, fontSize: 12.5, color: C.white, valign: 'top' });
    });
    footer(s, true);
    s.addNotes(`[~2 min] The numbers as submitted in the RFI: EMR 0.95 in 2024, 0.62 in 2025, 0.48 in 2026, roughly half the industry baseline and down 49% in two years. Active in ISNetworld with an A grade. No fatalities in the last three years. OSHA 300 logs for three years were provided with the RFI.
Let the trend speak: this is a sustained improvement, not a single good year.`);
  }

  // =====================================================================
  // 17. RISK MITIGATION PRACTICES
  {
    const s = pres.addSlide();
    bg(s, C.white);
    s.addImage({ path: IMG + 'slot_danger.jpg', x: 0, y: 0, w: 3.9, h: H });
    const X = 4.4;
    chip(s, '07', 'Safety & risk mitigation', false, X);
    title(s, 'Risk mitigation in the field', false, { x: X, w: 8.3 });
    const cards = [
      ['FaClipboardCheck', 'JSA & permits', 'Job-specific JSA reviewed at every shift change; daily toolbox talks'],
      ['FaLock', 'Isolation first', "Marathon's isolation and LOTO verified before any connection is made"],
      ['FaTachometerAlt', 'Pressure control', 'Normal 150–300 psi; over-pressure checklist above 500 psi'],
      ['FaExclamationTriangle', 'Line of fire', 'Bleed to zero at every pig change; nobody in line with lids or hoses'],
      ['FaLink', 'Hose integrity', 'Tested & certified hard and flex pipe; whip checks on every connection'],
      ['FaHardHat', 'PPE & coil care', 'FRC and face shields; no galvanized metal on stainless'],
    ];
    for (let i = 0; i < cards.length; i++) {
      const [ic, h, d] = cards[i];
      const x = X + (i % 2) * 4.2, y = 1.8 + Math.floor(i / 2) * 1.55;
      s.addShape(pres.shapes.RECTANGLE, { x, y, w: 4.03, h: 1.42, fill: { color: C.light }, line: { color: C.light } });
      await iconCircle(s, ic, x + 0.25, y + 0.25, 0.62, C.dark, C.gold);
      txt(s, h, { x: x + 1.05, y: y + 0.22, w: 2.85, h: 0.4, fontSize: 15.5, bold: true, color: C.text, valign: 'middle' });
      txt(s, d, { x: x + 1.05, y: y + 0.66, w: 2.85, h: 0.75, fontSize: 11.5, color: C.muted, valign: 'top' });
    }
    txt(s, [{ text: 'Engineered for safety  ', options: { bold: true, color: C.text } }, { text: 'Retractable cam-actuated stairs, composite work platform, LED lighting', options: { color: C.muted } }],
      { x: X, y: 6.5, w: 8.3, h: 0.3, fontSize: 11 });
    footer(s, false, X);
    s.addNotes(`[~2 min] Six practices that carry most of the risk on a decoke:
JSAs and permits: job-specific JSAs, reviewed at every shift change, with daily toolbox talks.
Isolation: we don't connect until Marathon's isolation and LOTO are verified.
Pressure: normal pigging is 150 to 300 psi; the pump is rated 600 but realistically tops out at 500 to 550 after valve losses, and above 500 psi the crew runs an over-pressure checklist.
Line of fire: every pig change bleeds to zero, and nobody stands in line with lids or hoses.
Hoses: tested and certified hard and flex pipe with whip checks on every connection.
PPE: FRC, hard hat, glasses or face shield, gloves, steel toes, hearing and respiratory protection as required. On stainless coils, no galvanized metal touches the tubes.
The pumper itself is engineered for safety too: retractable cam-actuated stairs, a composite work platform, LED lighting, and a self-contained design that prevents spills.
Full detail is in the safety manual and SSHASP submitted with the RFI.`);
  }

  // =====================================================================
  // 18. BEST PRACTICES & INNOVATION
  {
    const s = pres.addSlide();
    bg(s, C.dark);
    s.addImage({ path: IMG + 'slot_diff.jpg', x: 9.33, y: 0, w: 4.0, h: H });
    chip(s, '08', 'Best practices, capabilities & innovation', true);
    title(s, 'What sets USA DeBusk apart', true, { w: 8.4 });
    const cards = [
      ['FaIndustry', 'Self-performed scope', 'Pigging, decoking and hydroblasting with our own equipment and SCAQMD rigs: one contractor, no subs'],
      ['FaCogs', 'Largest triple-pass fleet', 'The largest triple-pass pumper fleet in the world, with a spare pump on board even on a 2-pass heater'],
      ['FaDatabase', 'Data-driven execution', 'Durations built from recorded actuals across our heater history; digital pig logs and job reports'],
      ['FaSyncAlt', 'Best practices shared', 'Lessons-learned reviews feed toolbox talks, training updates and post-job reviews with Marathon'],
    ];
    for (let i = 0; i < cards.length; i++) {
      const [ic, h, d] = cards[i];
      const x = 0.6 + (i % 2) * 4.3, y = 2.05 + Math.floor(i / 2) * 2.35;
      s.addShape(pres.shapes.RECTANGLE, { x, y, w: 4.1, h: 2.15, fill: { color: C.char }, line: { color: C.char } });
      await iconCircle(s, ic, x + 0.3, y + 0.3, 0.72, C.gold, C.dark);
      txt(s, h, { x: x + 1.2, y: y + 0.35, w: 2.75, h: 0.6, fontSize: 17, bold: true, color: C.white, valign: 'middle' });
      txt(s, d, { x: x + 0.3, y: y + 1.18, w: 3.6, h: 0.9, fontSize: 12.5, color: C.soft, valign: 'top' });
    }
    footer(s, true);
    s.addNotes(`[~2 min] Four differentiators.
Self-performed: pigging, decoking and hydroblasting with in-house equipment and SCAQMD rigs, so one contractor covers the full scope without subs.
Triple-pass: we run the largest triple-pass pigging pumper fleet in the world. The TriMax runs up to three passes at once; on LAR's 2-pass heaters that third pump is an on-board spare, so a pump failure doesn't stop the job, and it can also drive a smart pig. We also offer closed-loop filtration and smart-pig support, so Marathon deals with one contractor.
Data-driven: our durations aren't guesses. They're built from recorded actuals on the heaters we've cleaned, and every job produces pig logs and a job report that feed the next estimate. On a 60-decoke program that compounds.
Best practices: captured in lessons-learned reviews and shared through toolbox talks, training updates and post-job reviews with the client. On LAR, Marathon sits in that loop.`);
  }

  // =====================================================================
  // 19. MPC REFERENCES MAP
  {
    const s = pres.addSlide();
    bg(s, C.dark);
    chip(s, '09', 'References & case studies', true);
    title(s, 'Trusted across the MPC system', true);
    s.addImage({ path: IMG + 'mpc_map.png', x: 0.5, y: 1.7, w: 8.4, h: 8.4 * 1160 / 1860 });
    txt(s, '9', { x: 9.7, y: 2.0, w: 3.0, h: 1.3, fontSize: 88, bold: true, color: C.gold });
    txt(s, 'Marathon refineries with USA DeBusk references', { x: 9.7, y: 3.3, w: 3.0, h: 0.75, fontSize: 16, bold: true, color: C.white, valign: 'top' });
    txt(s, [
      { text: 'Named contacts at 8 sites (Galveston Bay on request), listed in the appendix', options: { bullet: true, breakLine: true } },
      { text: 'Includes Martinez, CA, our West Coast MPC reference', options: { bullet: true, breakLine: true } },
      { text: 'Crude, coker and vacuum heater experience', options: { bullet: true } },
    ], { x: 9.7, y: 4.25, w: 3.05, h: 2.4, fontSize: 12.5, color: C.soft, valign: 'top', paraSpaceAfter: 10 });
    footer(s, true);
    s.addNotes(`[~1.5 min] You don't have to take our word for it: nine Marathon refineries, with named contacts at eight of them; Galveston Bay's contact is available on request. Catlettsburg, Salt Lake City, Martinez, Dickinson, St. Paul Park, Robinson, Galveston Bay, Garyville and Detroit.
Martinez is the closest comparison for LAR: a California MPC facility under the same state air rules.
The contact list is in the appendix and in the leave-behind. We'd encourage the team to call any of them.`);
  }

  // =====================================================================
  // 20. CASE STUDIES
  {
    const s = pres.addSlide();
    bg(s, C.white);
    chip(s, '09', 'References & case studies', false);
    title(s, 'Coker heater case studies & lessons learned', false);
    const cs = [
      ['CHS McPherson, KS: Coker HF-0012', '6-pass coker heater, planned decoke, 2025',
        [["12,036'", 'coil footage'], ['6', 'passes'], ['85 h', 'pigging']],
        'Hard coke held pigs in the radiant section.',
        'Stage heavy-duty scraper pigs for the radiant from day one, not as a mid-job change.'],
      ['Phillips 66 Ponca City, OK: H-28 & H-29', 'Two coker heaters, emergency 2024 vs planned 2025',
        [['172 h', 'emergency callout'], ['131 h', 'planned decoke'], ['−24%', 'hours']],
        'Same two heaters, cleaned once as an unplanned callout and once on a planned schedule.',
        'A planned cadence lets rig-in, pig sets and crew be pre-staged, the model we propose for LAR.'],
    ];
    cs.forEach(([h, d, stats, ch, lesson], i) => {
      const x = 0.6 + i * 6.17, y = 1.95, w = 5.96;
      s.addShape(pres.shapes.RECTANGLE, { x, y, w, h: 4.8, fill: { color: C.light }, line: { color: C.light } });
      txt(s, h, { x: x + 0.35, y: y + 0.3, w: w - 0.7, h: 0.4, fontSize: 17, bold: true, color: C.text });
      txt(s, d, { x: x + 0.35, y: y + 0.7, w: w - 0.7, h: 0.3, fontSize: 12, color: C.muted });
      stats.forEach(([n, l], k) => {
        const sx = x + 0.35 + k * 1.8;
        txt(s, n, { x: sx, y: y + 1.2, w: 1.75, h: 0.65, fontSize: 28, bold: true, color: C.text });
        txt(s, l, { x: sx, y: y + 1.85, w: 1.75, h: 0.3, fontSize: 11, color: C.muted });
      });
      txt(s, [{ text: 'Challenge  ', options: { bold: true, color: C.text } }, { text: ch, options: { color: C.muted } }],
        { x: x + 0.35, y: y + 2.45, w: w - 0.7, h: 0.8, fontSize: 13, valign: 'top' });
      s.addShape(pres.shapes.RECTANGLE, { x: x + 0.35, y: y + 3.35, w: w - 0.7, h: 1.2, fill: { color: C.dark }, line: { color: C.dark } });
      txt(s, [{ text: 'Lesson learned  ', options: { bold: true, color: C.gold } }, { text: lesson, options: { color: C.white } }],
        { x: x + 0.55, y: y + 3.45, w: w - 1.1, h: 1.0, fontSize: 13, valign: 'middle' });
    });
    footer(s, false);
    s.addNotes(`[~1.5 min] Two coker examples from our job records.
First: CHS McPherson, coker heater HF-0012, six passes, just over 12,000 feet of coil, 85 pigging hours on a planned decoke. The radiant held hard coke that stopped standard pigs. Lesson: on a coker, stage the heavy-duty pig set for the radiant from the start. We'll do that at LAR on every occurrence.
Second: Phillips 66 Ponca City, coker heaters H-28 and H-29, cleaned once as an emergency callout (172 hours) and a year later on a planned schedule (131 hours). The planned job pre-staged rig-in, pigs and crew. That's the model of a recurring program like LAR's.`);
  }

  // =====================================================================
  // 21. WHY USA DEBUSK
  {
    const s = pres.addSlide();
    bg(s, C.dark);
    s.addImage({ path: IMG + 'slot_why.jpg', x: 0, y: 0, w: W, h: H });
    s.addImage({ path: IMG + 'fade_left.png', x: 0, y: 0, w: W, h: H });
    chip(s, '10', 'Why USA DeBusk', true);
    title(s, 'Why USA DeBusk for LAR', true, { w: 7.5, fontSize: 36 });
    const pts = [
      ['Proven on MPC heaters', '9 MPC references; projects for every major North American refiner'],
      ['California-ready', 'CARB-registered Tier 4 fleet, Southern California footprint'],
      ['Resilient execution', 'Triple-pass TriMax: a spare pump on every 2-pass heater'],
      ['Verified clean', '4-point verification and joint sign-off on every pass'],
      ['Safe by the numbers', 'EMR 0.48, ISNetworld A, zero fatalities in 3 years'],
    ];
    for (let i = 0; i < pts.length; i++) {
      const [h, d] = pts[i];
      const y = 2.05 + i * 0.92;
      await iconCircle(s, 'FaCheck', 0.6, y + 0.05, 0.55, C.gold, C.dark);
      txt(s, h, { x: 1.35, y, w: 6, h: 0.35, fontSize: 18, bold: true, color: C.white });
      txt(s, d, { x: 1.35, y: y + 0.36, w: 6, h: 0.3, fontSize: 13, color: C.soft });
    }
    footer(s, true);
    s.addNotes(`[~1 min] Close with the five reasons, then open for questions.
"We know Marathon's system, our equipment is registered and ready for California, the triple-pass rig carries its own spare pump, you sign off on every pass, and we do it safely."`);
  }

  // =====================================================================
  // 22. Q&A
  {
    const s = pres.addSlide();
    bg(s, C.dark);
    s.addImage({ path: IMG + 'slot_qa.jpg', x: 0, y: 0, w: W, h: H, transparency: 72 });
    s.addImage({ path: IMG + 'logo_white.png', x: (W - 4.0) / 2, y: 1.6, w: 4.0, h: 4.0 * 101 / 674 });
    txt(s, 'Thank you', { x: 0.6, y: 2.6, w: 12.13, h: 1.0, fontSize: 48, bold: true, color: C.white, align: 'center' });
    txt(s, 'Questions & discussion', { x: 0.6, y: 3.55, w: 12.13, h: 0.5, fontSize: 22, color: C.gold, align: 'center' });
    txt(s, [
      { text: 'Marshall Douglas  |  Director of Pigging Operations', options: { breakLine: true } },
      { text: 'Jason Harman  |  Commercial Manager  |  jharman@usadebusk.com  |  (713) 839-5961' },
    ], { x: 0.6, y: 5.3, w: 12.13, h: 0.8, fontSize: 14, color: C.white, align: 'center', paraSpaceAfter: 6 });
    s.addNotes(`[20 min reserved for Q&A]
Likely questions and where the answer lives:
- "How do you handle a plugged pass?" Bi-directional flow and stepwise pig sizing (slides 4–5); pre-job walkdown (slide 15).
- "What if duration overruns?" Lump sum per occurrence. Pricing excludes additional fouling, unknown repairs and stoppages outside our control; those, plus stand-by not caused by USA DeBusk, are billed T&M at the proposal rates.
- "Local presence?" Slide 16, per RFI GD-1.
- "CARB registration?" Slide 13: every TriMax carries statewide PERP registration.
- "Filtration?" Available at $150/hr per the rate sheet.
- "Pump curves / pressure capability?" Appendix slide 25 (Waterous CMU curves). Normal 150–300 psi; rated 600, 500–550 effective after valve losses.`);
  }

  // =====================================================================
  // 23. APPENDIX — MPC REFERENCES
  {
    const s = pres.addSlide();
    bg(s, C.white);
    chip(s, null, 'Appendix', false);
    title(s, 'MPC references', false, { fontSize: 28 });
    const hdr = (t) => ({ text: t, options: { bold: true, color: C.white, fill: { color: C.dark }, fontSize: 10.5 } });
    const refs = [
      ['Catlettsburg, KY', 'Eddie Slone', 'T/A Planner', '606-331-2585', 'slone@marathonpetroleum.com'],
      ['', 'Ryan Rayburn', 'TAR / Construction Supervisor', '606-331-0180', 'rdrayburn@marathonpetroleum.com'],
      ['', 'Ben Holbrook', 'Turnaround Planning', '606-369-6467', 'benlholbrook@marathonpetroleum.com'],
      ['Salt Lake City, UT', 'Aaron Wiggins', 'Maintenance Supervisor / Turnarounds', '801-703-6722', 'ATWiggins@marathonpetroleum.com'],
      ['Martinez, CA', 'Kyle Yates', 'Project Engineer', '925-316-9726', 'SYates2@marathonpetroleum.com'],
      ['', 'Ryan Gorman', '', '952-607-6853', 'RMGorman@marathonpetroleum.com'],
      ['Dickinson, ND', 'Tyler Bauer', 'TA', '701-516-3456', 'tbauer@marathonpetroleum.com'],
      ['St. Paul Park, MN', 'Keith James', 'TA Planner', '715-441-7986', 'TKJames@marathonpetroleum.com'],
      ['Robinson, IL', 'Brian Maus', 'TA', '618-544-2121', 'bkmaus@marathonpetroleum.com'],
      ['Galveston Bay, TX', 'Available upon request', '', '', ''],
      ['Garyville, LA', 'Shawn Kramer', 'TA Planner', '225-571-2689', 'skramer@marathonpetroleum.com'],
      ['', 'Chad Childs', 'TA Supervisor', '281-299-6088', 'cechilds@marathonpetroleum.com'],
      ['Detroit, MI', 'Nate Lajiness', 'Turnaround Planner', '313-297-6166', 'nlajiness@marathonpetroleum.com'],
    ];
    const rows = [[hdr('Refinery'), hdr('Contact'), hdr('Role'), hdr('Phone'), hdr('Email')]]
      .concat(refs.map((r, i) => r.map((c, k) => ({ text: c, options: { fill: { color: i % 2 ? 'F7F7F7' : C.white }, color: C.text, fontSize: 10, bold: k === 0 } }))));
    s.addTable(rows, { x: 0.6, y: 1.75, w: 12.13, colW: [2.0, 2.2, 3.1, 1.55, 3.28], rowH: 0.33, fontFace: FONT, border: { type: 'solid', pt: 0.5, color: C.rule }, valign: 'middle', margin: [0, 0.08, 0, 0.08] });
    footer(s, false);
    s.addNotes(`Leave-behind reference list. Not presented; point to it from slide 20 (MPC map) if asked.`);
  }

  // =====================================================================
  // 24. APPENDIX — PUMP CURVES
  {
    const s = pres.addSlide();
    bg(s, C.white);
    chip(s, null, 'Appendix', false);
    title(s, 'TriMax pump performance', false, { fontSize: 28 });
    sub(s, 'Waterous CMU two-stage pump, one per pass. Series operation is used for pigging.', false);
    const ih = 4.45, iw = ih * PCW / PCH;
    s.addShape(pres.shapes.RECTANGLE, { x: 0.55, y: 2.1, w: iw + 0.1, h: ih + 0.1, fill: { color: C.white }, line: { color: C.rule, width: 1 } });
    s.addImage({ path: IMG + 'pump_curve.png', x: 0.6, y: 2.15, w: iw, h: ih });
    txt(s, 'Manufacturer curves: Waterous Company, form F-2692', { x: 0.6, y: 2.25 + ih, w: iw, h: 0.25, fontSize: 9.5, italic: true, color: C.grey });
    const k = [['150–300', 'psi normal pigging'], ['500–550', 'psi effective max, after valve losses'], ['600', 'psi rated pump maximum']];
    k.forEach(([n, l], i) => {
      const y = 2.15 + i * 1.5;
      s.addShape(pres.shapes.RECTANGLE, { x: 8.55, y, w: 4.18, h: 1.3, fill: { color: i === 0 ? C.dark : C.light }, line: { color: i === 0 ? C.dark : C.light } });
      txt(s, n, { x: 8.8, y: y + 0.12, w: 3.7, h: 0.6, fontSize: 28, bold: true, color: i === 0 ? C.gold : C.text, valign: 'middle' });
      txt(s, l, { x: 8.8, y: y + 0.72, w: 3.7, h: 0.45, fontSize: 11.5, color: i === 0 ? C.white : C.muted, valign: 'top' });
    });
    footer(s, false);
    s.addNotes(`Backup slide, not presented. Pull it up if an engineer asks about pump capability.
Series operation is how the pump runs for pigging (higher pressure, lower flow). Normal pigging runs 150 to 300 psi. The curve tops out at 600 psi; in practice we see 500 to 550 at the pig because of losses through our valves.`);
  }

  await pres.writeFile({ fileName: __dirname + '/LAR_Technical_Proposal_Presentation.pptx' });
  console.log('written');
})();
