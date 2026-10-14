// Valero Texas City — Heater Pigging & Decoking capabilities presentation.
// Forked from the Marathon LAR deck (02-facilities/Marathon/Carson-CA/DSP26098-technical-presentation/build/build.js).
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
  pres.title = 'Valero Texas City — Heater Pigging & Decoking Services';

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
    txt(slide, 'USA DeBusk  |  Valero Texas City  |  Heater Pigging & Decoking Services', { x: fx, y: 7.02, w: 8, h: 0.25, fontSize: 9, color: dark ? C.soft : '9A9A9A' });
    txt(slide, String(pageNo + 1), { x: 12.2, y: 7.02, w: 0.53, h: 0.25, fontSize: 9, color: dark ? C.soft : '9A9A9A', align: 'right' });
  };

  const bg = (slide, color) => { slide.background = { color }; };

  const shadow = () => ({ type: 'outer', color: '000000', blur: 8, offset: 2, angle: 90, opacity: 0.12 });

  const iconCircle = async (slide, name, x, y, d, circleColor, iconColor) => {
    slide.addShape(pres.shapes.OVAL, { x, y, w: d, h: d, fill: { color: circleColor }, line: { color: circleColor } });
    const pad = d * 0.25;
    slide.addImage({ data: await icon(name, iconColor), x: x + pad, y: y + pad, w: d - 2 * pad, h: d - 2 * pad });
  };

  // Location badge: gold label on a charcoal pill
  const locBadge = (slide, label, tw, right = 12.73, y = 0.34) => {
    const h = 0.62, w = tw + 0.5, x = right - w;
    slide.addShape(pres.shapes.ROUNDED_RECTANGLE, { x, y, w, h, fill: { color: C.char }, line: { color: C.gold, width: 1 }, rectRadius: 0.1 });
    txt(slide, label, { x, y, w, h, fontSize: 11, bold: true, color: C.gold, align: 'center', valign: 'middle' });
  };

  // =====================================================================
  // 1. TITLE
  {
    const s = pres.addSlide();
    bg(s, C.dark);
    s.addImage({ path: IMG + 'cover_trimax.jpg', x: 5.0, y: 0, w: W - 5.0, h: H });
    s.addShape(pres.shapes.RECTANGLE, { x: 0.7, y: 2.1, w: 0.9, h: 0.07, fill: { color: C.gold }, line: { color: C.gold } });
    s.addImage({ path: IMG + 'logo_white.png', x: 0.7, y: 0.65, w: 3.4, h: 3.4 * 101 / 674 });
    txt(s, 'Heater Pigging\n& Decoking\nServices', { x: 0.7, y: 2.35, w: 4.2, h: 2.1, fontSize: 38, bold: true, color: C.white, valign: 'top', lineSpacingMultiple: 0.95 });
    txt(s, 'Valero Texas City Refinery', { x: 0.7, y: 4.5, w: 4.2, h: 0.45, fontSize: 18, color: C.gold, bold: true });
    txt(s, 'Mechanical pigging & decoking for fired heaters', { x: 0.7, y: 4.95, w: 4.2, h: 0.6, fontSize: 14, color: C.soft, valign: 'top' });
    txt(s, [
      { text: 'Presented by Jason Harman', options: { bold: true, color: C.white, breakLine: true } },
      { text: 'Commercial Manager', options: { color: C.soft, breakLine: true } },
      { text: 'October 2026', options: { color: C.grey } },
    ], { x: 0.7, y: 5.85, w: 4.2, h: 1.0, fontSize: 13, valign: 'top', paraSpaceAfter: 2 });
    s.addNotes(`[~1 min] Open: thank the Texas City team for the time. Introduce yourself (Jason Harman, Commercial Manager) and anyone attending with you.
Frame: "We're not new to Texas City: we pigged your H-57 coker heater in 2023 and again in 2024. This is an overview of how we pig and decoke fired heaters, what we bring to site, and what we've done across the Valero system. About 30 minutes, then questions."
The photo is TriMax 4 staged at a refinery, the same equipment we'd bring to Texas City.`);
  }

  // =====================================================================
  // 2. AGENDA
  {
    const s = pres.addSlide();
    bg(s, C.dark);
    s.addShape(pres.shapes.RECTANGLE, { x: 0, y: 0, w: 0.18, h: H, fill: { color: C.gold }, line: { color: C.gold } });
    txt(s, 'Agenda', { x: 0.9, y: 0.6, w: 7, h: 0.7, fontSize: 34, bold: true, color: C.white });
    txt(s, 'Heater pigging & decoking at Texas City', { x: 0.9, y: 1.3, w: 7.5, h: 0.4, fontSize: 15, color: C.soft });
    s.addImage({ path: IMG + 'logo_white.png', x: W - 0.6 - 2.6, y: 0.75, w: 2.6, h: 2.6 * 101 / 674 });
    const items = ['Pigging & decoking methodology', 'Execution', 'Readiness & resources', 'Equipment & technology', 'Cleanliness verification & QA/QC',
      'Emergency response', 'Safety & risk mitigation', 'Capabilities', 'Valero references & case study', 'Why USA DeBusk'];
    items.forEach((it, i) => {
      const col = i < 5 ? 0 : 1, row = i % 5;
      const x = 0.9 + col * 6.0, y = 2.3 + row * 0.9;
      txt(s, String(i + 1).padStart(2, '0'), { x, y, w: 0.85, h: 0.6, fontSize: 30, bold: true, color: C.gold, valign: 'middle' });
      txt(s, it, { x: x + 0.95, y, w: 4.6, h: 0.6, fontSize: 18, color: C.white, valign: 'middle' });
      s.addShape(pres.shapes.LINE, { x, y: y + 0.72, w: 5.4, h: 0, line: { color: C.char2, width: 1 } });
    });
    s.addNotes(`[~0.5 min] Walk the agenda quickly: how we clean a heater, how we run the job, what we bring, how you know it's clean, safety, and our Valero track record.
Transition: "First, the services we offer a site like Texas City."`);
  }

  // =====================================================================
  // 3. SCOPE UNDERSTANDING
  {
    const s = pres.addSlide();
    bg(s, C.white);
    s.addImage({ path: IMG + 'onsite_40.jpg', x: 9.33, y: 0, w: 4.0, h: H });
    chip(s, null, 'Services', false);
    title(s, 'Our services for Texas City', false, { w: 8.4 });
    sub(s, 'Mechanical decoking of fired heater coils, planned or on short notice', false, { w: 8.4 });
    const cards = [
      ['FaFire', 'Coker heaters', 'Hard coke in radiant and convection coils, on run-length or turnaround cycles'],
      ['FaIndustry', 'Crude & vacuum heaters', 'Pitch, resid and coke across mixed-diameter passes'],
      ['FaCogs', 'Charge & process heaters', 'Process heater coils cleaned and verified ahead of restart or inspection'],
      ['FaSearch', 'Smart pig support', 'Coils cleaned to inspection standard; spare TriMax pump drives the inspection tool'],
    ];
    for (let i = 0; i < cards.length; i++) {
      const [ic, h, d] = cards[i];
      const x = 0.6 + (i % 2) * 4.25, y = 2.3 + Math.floor(i / 2) * 1.6;
      s.addShape(pres.shapes.RECTANGLE, { x, y, w: 4.08, h: 1.45, fill: { color: C.light }, line: { color: C.light } });
      await iconCircle(s, ic, x + 0.25, y + 0.28, 0.62, C.dark, C.gold);
      txt(s, h, { x: x + 1.05, y: y + 0.2, w: 2.9, h: 0.4, fontSize: 15.5, bold: true, color: C.text, valign: 'middle' });
      txt(s, d, { x: x + 1.05, y: y + 0.62, w: 2.9, h: 0.75, fontSize: 11.5, color: C.muted, valign: 'top' });
    }
    const tiles = [['Planned', 'turnarounds & run-length decokes'], ['Short notice', 'emergency mobilization'], ['Optional', 'closed-loop filtration']];
    tiles.forEach(([n, l], i) => {
      const x = 0.6 + i * 2.83, y = 5.65;
      s.addShape(pres.shapes.RECTANGLE, { x, y, w: 2.66, h: 1.15, fill: { color: C.dark }, line: { color: C.dark } });
      txt(s, n, { x: x + 0.2, y: y + 0.1, w: 2.3, h: 0.5, fontSize: 20, bold: true, color: C.gold, valign: 'middle' });
      txt(s, l, { x: x + 0.2, y: y + 0.6, w: 2.3, h: 0.45, fontSize: 11, color: C.white, valign: 'top' });
    });
    footer(s, false);
    s.addNotes(`[~1.5 min] What we do, in one slide. We mechanically pig and decoke fired heater coils: cokers, crude and vacuum heaters, and charge and process heaters. The method is the same across all of them; what changes is the coke, the coil geometry and the metallurgy, and we plan each heater around those.
Smart pig support: we clean coils to the standard an inspection tool needs, and the TriMax's spare pump can drive the inspection pig, so the inspection doesn't need its own pumping equipment.
We work planned turnarounds and run-length decokes, and we mobilize on short notice when a heater has to come down. Closed-loop filtration is available as an option; we'll cover it in the equipment section.
Transition: "Here's how we clean a pass."`);
  }

  // =====================================================================
  // 4. METHODOLOGY — PROCESS
  {
    const s = pres.addSlide();
    bg(s, C.white);
    s.addImage({ path: IMG + 'slot_method_t6.jpg', x: 9.33, y: 0, w: 4.0, h: H });
    chip(s, '01', 'Methodology', false);
    title(s, 'Bi-directional mechanical decoking', false, { w: 8.4 });
    sub(s, 'Every pass follows the same controlled sequence', false, { w: 8.4 });
    const steps = [
      ['Rig-in & pressure test', 'Connect 300# launchers and receivers; fill and test before any launch'],
      ['Baseline flow test', 'Record pressure at a set rate for a before-and-after comparison'],
      ['Gauge foam run', 'Proves the pass is open and sets the initial pig size'],
      ['Scraper pig progression', 'Carbide-studded pigs run in both directions, stepped up ⅛" per clean pass'],
      ['Oversize polish', 'Up to tube ID + ¼" maximum, with real-time pressure monitoring'],
      ['Gauge foam & sign-off', 'Line-size foam witnessed by Valero, final flow test, pass signed clean'],
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
Step 6: Valero witnesses the final gauge foam and signs off per pass (detail on slide 15).`);
  }

  // =====================================================================
  // 5. PIG PROGRESSION PLAN
  {
    const s = pres.addSlide();
    bg(s, C.white);
    chip(s, '01', 'Methodology', false);
    title(s, 'Pig progression plan', false);
    sub(s, 'The gauge foam run sets the starting size; the smallest tube ID sets the ceiling', false);
    const plans = [
      ['Example: 4" Sch 80 coil', 'Tube ID 3.826"', ['Gauge\nfoam', 'Initial', '+⅛"', '+⅛"', '+⅛"', '3.826"', '4.076"']],
      ['Example: mixed-diameter pass, 3" to 8"', 'Smallest ID 2.900" governs the whole pass', ['Gauge\nfoam', 'Initial', '+⅛"', '+⅛"', '+⅛"', '2.900"', '3.150"']],
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
      { text: 'Body length set for bends & mule ears', options: { bullet: true, breakLine: true } },
      { text: 'Gauge foam sets the starting size', options: { bullet: true, breakLine: true } },
      { text: 'Line-size foam witnessed at sign-off', options: { bullet: true } },
    ], { x: 9.05, y: 4.0, w: 3.5, h: 2.5, fontSize: 13, color: C.soft, valign: 'top', paraSpaceAfter: 12 });
    footer(s, false);
    s.addNotes(`[~2 min] Every heater gets a pig progression plan before we mobilize; these are two examples of how it's built.
The ceiling is fixed by our sizing rule: smallest tube ID plus a quarter inch. On a 4" Sch 80 coil the ID is 3.826", so the maximum is 4.076". Where a pass changes diameter, as on many vacuum heaters, the smallest ID governs the whole pass: a pass running 3" to 8" is capped by its 2.900" tubes. Tube condition can set a lower practical ceiling, and when it does, we stop there.
We don't pick a starting size in advance. The first run is a gauge foam: how it comes out of the pass tells us how much the bore is restricted, and that sets the initial pig size. From there we step up 1/8" at a time, only after a clean pass at the current size, until we reach line size and then the maximum. Wear marks on a pig show where coke remains, and we change size and appendage type from that evidence.
If asked about short-radius bends or mule ears: pig body length and flexibility are selected for the bend geometry, not just the diameter.`);
  }

  // =====================================================================
  // 5b. ENGINEERED DECOKING PIGS
  {
    const s = pres.addSlide();
    bg(s, C.white);
    chip(s, '01', 'Methodology', false);
    title(s, 'Engineered decoking pigs, matched to the coke', false);
    sub(s, 'The most diverse selection of engineered decoking pigs in the world', false);
    // photo panel
    s.addShape(pres.shapes.RECTANGLE, { x: 0.6, y: 2.25, w: 4.0, h: 4.5, fill: { color: C.white }, line: { color: C.rule, width: 1 } });
    s.addImage({ path: IMG + 'pigs_new.jpg', x: 0.85, y: 3.05, w: 3.5, h: 3.5 * 215 / 330 });
    txt(s, 'New engineered decoking pigs', { x: 0.85, y: 6.1, w: 3.5, h: 0.3, fontSize: 10.5, italic: true, color: C.muted, align: 'center' });
    const cards = [
      ['FaLayerGroup', 'Soft-core and hard-core designs', 'Urethane or high-density foam bodies, plus foam pushers for flushing and proving the pass'],
      ['FaSlidersH', 'A full range of durometers', 'Soft to hard compounds, chosen to compress through tight bends or cut hard coke'],
      ['FaDotCircle', 'Bald or studded', 'Tungsten carbide, hardened-steel and stainless stud options, matched to the tube metallurgy'],
      ['FaHammer', 'Heavy-coke designs', 'High-durometer, fully studded pigs brought in when pig wear shows hard, heavy coke'],
    ];
    for (let i = 0; i < cards.length; i++) {
      const [ic, h, d] = cards[i];
      const x = 4.95 + (i % 2) * 3.95, y = 2.25 + Math.floor(i / 2) * 2.3;
      s.addShape(pres.shapes.RECTANGLE, { x, y, w: 3.78, h: 2.15, fill: { color: C.light }, line: { color: C.light } });
      await iconCircle(s, ic, x + 0.28, y + 0.28, 0.66, C.dark, C.gold);
      txt(s, h, { x: x + 1.1, y: y + 0.3, w: 2.55, h: 0.62, fontSize: 15, bold: true, color: C.text, valign: 'middle' });
      txt(s, d, { x: x + 0.28, y: y + 1.12, w: 3.25, h: 0.9, fontSize: 12, color: C.muted, valign: 'top' });
    }
    footer(s, false);
    s.addNotes(`[~1.5 min] The pig does the work, so pig selection matters as much as the pumper.
(Presenter: this is where to talk about our supplier base and why we source rather than build.)
Walk the four cards. Bodies come soft-core or hard-core, in urethane or high-density foam, plus medium and hard foam pushers. Durometers run across a full range (for example 40, 60 and 80) so we can compress through tight bends or cut hard coke. Pigs run bald or studded: tungsten carbide, hardened steel, or stainless where the tube metallurgy calls for it. And when pig wear shows hard, heavy coke, we move to high-durometer, fully studded designs.
The photo shows new pigs: soft and hard bodies, bald and studded.`);
  }

  // =====================================================================
  // 6. HEATER DATA & COIL CONTROLS
  {
    const s = pres.addSlide();
    bg(s, C.light);
    chip(s, '01', 'Methodology', false);
    title(s, 'Coil-specific controls', false);
    sub(s, 'Every heater is planned from its drawings before we mobilize', false);
    const cards = [
      ['FaRulerCombined', 'Tube geometry', 'Footage, tube IDs and diameter changes per pass set the pig progression and the duration'],
      ['FaTint', 'Metallurgy', 'Stainless and chrome coils: water quality verified before fill, no galvanized contact with tubes'],
      ['FaLink', 'Connections', 'Coil flange size and rating confirmed; spools and adapters matched to our 300# launchers and receivers'],
      ['FaSyncAlt', 'Return bends', 'Pig length and flexibility selected for 180° returns, plug headers and mule ears'],
      ['FaLayerGroup', 'Launcher access', 'Inlet and outlet elevations walked down; rig layout set before rig-in'],
      ['FaFire', 'Coke & service', 'Coker, crude or vacuum service sets the pig set staged on day one'],
    ];
    for (let i = 0; i < cards.length; i++) {
      const [ic, h, d] = cards[i];
      const x = 0.6 + (i % 3) * 4.1, y = 2.3 + Math.floor(i / 3) * 2.25;
      s.addShape(pres.shapes.RECTANGLE, { x, y, w: 3.93, h: 2.05, fill: { color: C.white }, line: { color: C.white }, shadow: shadow() });
      await iconCircle(s, ic, x + 0.28, y + 0.28, 0.66, C.dark, C.gold);
      txt(s, h, { x: x + 1.1, y: y + 0.3, w: 2.7, h: 0.62, fontSize: 16, bold: true, color: C.text, valign: 'middle' });
      txt(s, d, { x: x + 0.28, y: y + 1.08, w: 3.4, h: 0.9, fontSize: 12, color: C.muted, valign: 'top' });
    }
    footer(s, false);
    s.addNotes(`[~1.5 min] We don't show up and figure out the heater on site. Every heater is planned from its drawings first.
Geometry: footage and tube IDs per pass, and where the diameter changes, set the pig progression and the duration estimate.
Metallurgy: on stainless and chrome coils we verify water quality before fill and keep galvanized hardware off the tubes.
Connections: we confirm the coil flange size and rating and match the spools and adapters to our 300# launchers and receivers before we arrive.
Bends: 180° returns, plug headers and mule ears set pig length and flexibility, not just diameter.
Access: inlet and outlet elevations get walked down so the rig layout is set before rig-in.
Service: a coker, a crude heater and a vacuum heater foul differently, and that decides which pigs we stage from day one.
If Texas City shares drawings for a heater, we'll build its plan the same way.`);
  }

  // =====================================================================
  // 7. EXECUTION PLAN — GANTT
  {
    const s = pres.addSlide();
    bg(s, C.white);
    chip(s, '02', 'Execution', false);
    title(s, 'How a decoke runs', false);
    sub(s, 'Continuous 24/7 pigging on 12-hour shifts; passes pigged in conjunction', false);
    const steps = [
      ['Plan', 'Drawings reviewed, pig progression and rig layout set'],
      ['Rig-in', 'Launchers and receivers connected, filled and pressure tested'],
      ['Pig', 'Up to three passes at once per TriMax, around the clock'],
      ['Rig-over', 'Move to the next set of passes, if the heater has more'],
      ['Verify', 'Final gauge foam and flow test, pass signed off with Valero'],
      ['Rig-out', 'Equipment out, job book delivered'],
    ];
    const n = steps.length, gap = 0.12, bw = (12.13 - gap * (n - 1)) / n, y0 = 2.45;
    steps.forEach(([h, d], i) => {
      const x = 0.6 + i * (bw + gap);
      const pig = h === 'Pig', ro = h === 'Rig-over';
      const fill = pig ? C.gold : (ro ? C.soft : C.dark);
      s.addShape(pres.shapes.CHEVRON, { x, y: y0, w: bw, h: 0.9, fill: { color: fill }, line: { color: fill } });
      txt(s, h, { x: x + 0.25, y: y0, w: bw - 0.5, h: 0.9, fontSize: 15, bold: true, color: pig || ro ? C.dark : C.white, align: 'center', valign: 'middle' });
      txt(s, d, { x: x + 0.05, y: y0 + 1.05, w: bw - 0.1, h: 1.0, fontSize: 11.5, color: C.muted, align: 'center', valign: 'top' });
    });
    const st = [['24/7', 'two 12-hour shifts until the heater is handed back'], ['Up to 3', 'passes pigged at once on each TriMax'], ['2+', 'TriMax units on larger heaters or multi-heater jobs']];
    st.forEach(([v, l], i) => {
      const x = 0.6 + i * 4.1;
      s.addShape(pres.shapes.RECTANGLE, { x, y: 4.9, w: 3.93, h: 1.55, fill: { color: C.light }, line: { color: C.light } });
      txt(s, v, { x: x + 0.25, y: 5.0, w: 3.5, h: 0.75, fontSize: 32, bold: true, color: C.text, valign: 'middle' });
      txt(s, l, { x: x + 0.25, y: 5.75, w: 3.5, h: 0.55, fontSize: 12, color: C.muted, valign: 'top' });
    });
    footer(s, false);
    s.addNotes(`[~2 min] Every decoke follows the same sequence.
Plan: the heater's drawings set the pig progression, the rig layout and the duration estimate before we arrive.
Rig-in: launchers and receivers connected, filled and pressure tested before anything launches.
Pig: "in conjunction" means passes are pigged at the same time, each on its own pump and operator station, so elapsed time is one pass's time, not the sum. A TriMax runs up to three passes at once; on a heater with fewer passes, the spare pump keeps the job running if a pump goes down.
Rig-over: on heaters with more passes than pumps, we move to the next set. Larger heaters or multi-heater jobs get more than one TriMax.
Verify and rig-out: each pass is signed off with Valero, then the equipment comes out and the job book is delivered.
We run 24/7 on 12-hour day and night shifts until the heater is handed back. Duration depends on footage and on how hard and thick the deposits are, and we quote each heater from its own geometry.`);
  }

  // =====================================================================
  // 9. OPERATIONAL READINESS & RESOURCES
  {
    const s = pres.addSlide();
    bg(s, C.white);
    s.addImage({ path: IMG + 'slot_ready.jpg', x: 0, y: 0, w: 4.6, h: H });
    const X = 5.1;
    chip(s, '03', 'Readiness & resources', false, X);
    title(s, 'Crew & equipment, every job', false, { x: X, w: 7.6, fontSize: 30 });
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
    s.addNotes(`[~1.5 min] A standard single-rig job gets this package: one TriMax, one support unit carrying fittings, tooling and spares, two crew trucks. Bigger heaters get more rigs and more crew.
Crew: day shift is a supervisor and two operators; night shift is a supervisor and an operator; a project manager owns the job and the daily updates.
Readiness: turnover has run about 5% over the last 12 months. We hold onto people with competitive pay, ongoing training and certification, career paths, and dedicated core crews per site. For Texas City that means the same faces on your heaters job after job.
Every technician is USA DeBusk-certified, selected by heater-type experience, with training verified before mobilization. Our personnel training documents are available on request.`);
  }

  // =====================================================================
  // 10. PROJECT TEAM ORG CHART
  {
    const s = pres.addSlide();
    bg(s, C.dark);
    chip(s, '03', 'Readiness & resources', true);
    title(s, 'Our pigging team', true);
    // experience tiles
    [['210', 'years of combined pigging & decoking experience'], ['15+', 'years self-performing heater pigging']].forEach(([n, l], i) => {
      const y = 1.9 + i * 1.55;
      s.addShape(pres.shapes.RECTANGLE, { x: 0.6, y, w: 3.3, h: 1.35, fill: { color: C.char }, line: { color: C.gold, width: 1 } });
      txt(s, n, { x: 0.8, y: y + 0.1, w: 2.9, h: 0.68, fontSize: 36, bold: true, color: C.gold, valign: 'middle' });
      txt(s, l, { x: 0.8, y: y + 0.78, w: 2.9, h: 0.5, fontSize: 11.5, color: C.white, valign: 'top' });
    });
    const ln = (x, y, w, h) => s.addShape(pres.shapes.LINE, { x, y, w, h, line: { color: C.grey, width: 1.25 } });
    const box = (x, y, w, h, name, role, yrs, gold, small) => {
      s.addShape(pres.shapes.RECTANGLE, { x, y, w, h, fill: { color: gold ? C.gold : C.char }, line: { color: gold ? C.gold : C.char2 } });
      const fs = small ? 11.5 : 13.5, rs = small ? 9.5 : 10.5;
      const nameW = small ? w - 0.25 : w - 0.9;
      txt(s, name, { x: x + 0.14, y: y + 0.06, w: nameW, h: h * 0.45, fontSize: fs, bold: true, color: gold ? C.dark : C.white, valign: 'middle' });
      txt(s, role, { x: x + 0.14, y: y + h * 0.5, w: small ? w - 0.72 : w - 0.9, h: h * 0.42, fontSize: small ? 9 : rs, color: gold ? C.dark : C.soft, valign: 'middle' });
      const yY = small ? y + h * 0.5 : y + 0.06, yH = small ? h * 0.42 : h * 0.45;
      txt(s, yrs + ' yrs', { x: x + w - (small ? 0.62 : 0.8), y: yY, w: small ? 0.52 : 0.7, h: yH, fontSize: small ? 10.5 : 12, bold: true, color: gold ? C.dark : C.gold, align: 'right', valign: 'middle' });
    };
    // top of chart
    const cx = 8.55, bw = 3.2, bh = 0.72;
    box(cx - bw / 2, 1.85, bw, bh, 'Anthony Fazio', 'Vice President of Operations', 20);
    ln(cx, 1.85 + bh, 0, 0.2);
    box(cx - bw / 2, 2.77, bw, bh, 'Marshall Douglas', 'Director of Pigging Operations', 26);
    ln(cx, 2.77 + bh, 0, 0.14);
    const l3x = [cx - 1.8, cx + 1.8];
    ln(l3x[0], 3.63, l3x[1] - l3x[0], 0);
    ln(l3x[0], 3.63, 0, 0.1); ln(l3x[1], 3.63, 0, 0.1);
    box(l3x[0] - bw / 2 + 0.05, 3.73, bw - 0.1, bh, 'Jason Harman', 'Commercial Manager', 22, true);
    box(l3x[1] - bw / 2 + 0.05, 3.73, bw - 0.1, bh, 'Travis Trenholm', 'Pigging Operations Manager', 15);
    // team under Travis
    const team = [
      ['Danilo Ramirez', 'Project Manager', 33], ['Jesse Utsey', 'Project Manager', 23], ['Sid Servin', 'Equipment Manager', 18], ['Danny Harman', 'Field Tech', 25],
      ['Dacorey Slater', 'Project Manager', 8], ['James Lee', 'Project Manager', 10], ['James McDaniel', 'Project Manager', 5], ['Rodney Lynch', 'Project Manager', 5],
    ];
    const gx0 = 4.25, gw = 2.05, gg = 0.1, gh = 0.66, gy0 = 4.93;
    ln(l3x[1], 3.73 + bh, 0, 0.14);
    const spanL = gx0 + gw / 2, spanR = gx0 + 3 * (gw + gg) + gw / 2;
    ln(spanL, 4.59, spanR - spanL, 0);
    ln(l3x[1], 4.59, 0, 0);
    team.forEach(([n, r, y], i) => {
      const col = i % 4, row = Math.floor(i / 4);
      const x = gx0 + col * (gw + gg), yy = gy0 + row * (gh + 0.12);
      if (row === 0) ln(x + gw / 2, 4.59, 0, gy0 - 4.59);
      box(x, yy, gw, gh, n, r, y, false, true);
    });
    footer(s, true);
    s.addNotes(`[~1 min] Our team brings 210 years of combined pigging and decoking experience, and the company has self-performed heater pigging for over 15 years.
Leadership: Anthony Fazio, VP Operations, 20 years; Marshall Douglas, Director of Pigging Operations, 26 years. I'm Jason Harman, Commercial Manager, 22 years, and I'm your commercial point of contact. Travis Trenholm, Pigging Operations Manager, 15 years, runs the field operation.
Under Travis: a bench of project managers, our equipment manager and a senior field tech, led in experience by Danilo Ramirez at 33 years. On every job one project manager is the single point of contact for the work flow and daily updates to Valero.`);
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
    sub(s, '6 identical TriMax units, 18 engines: one standardized fleet', true, { w: 7 });
    const specs = [
      ['FaCogs', 'Three independent pump systems', 'Closed-loop, bi-directional; 50% more productive than a twin pumper'],
      ['FaDesktop', 'Automated HMI control', 'Three 17" touchscreens, automated digital pig logs'],
      ['FaTachometerAlt', '150–300 psi working pressure', 'Pump rated 600 psi; 500–550 psi effective after valve losses'],
      ['FaChartLine', 'Real-time sensor data', 'Coke shows as pressure spikes at the operator interface'],
      ['FaLeaf', 'Cummins QSL9, 333 bhp, Tier 4 Final', 'The same engine across all 18 pumps in the fleet'],
    ];
    for (let i = 0; i < specs.length; i++) {
      const [ic, h, d] = specs[i];
      const y = 2.2 + i * 0.8;
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
    s.addNotes(`[~1.5 min] This is the core of our service, and every one of our six TriMax units is the same build: 18 identical engines, the same pumps, the same controls. Any crew can run any unit, spares fit every unit, and the procedures are the same everywhere. Three independent pump assemblies in one trailer, each with its own operator station, so three passes can run at the same time. Against a dual unit the triple raises productivity by about 50%, and on a two-pass heater the third pump is 100% spare capacity: if one pump goes down, the job doesn't stop.
The spare pump can also propel a smart pig, so inspection runs don't need extra equipment.
Each operator station has a 17" automated HMI touchscreen, and pig logs are recorded digitally (operator screen, two slides on).
Other features built into the unit: temperature-controlled pig compartments so the pigs keep their cleaning characteristics, antifoam injection, a coke transfer chute, and guided-radar tank level indicators. On-board tankage is 3,000 gal clean and 2,000 gal return.
The bar at the bottom is our operating window, 150 to 300 psi for normal pigging; the next slide shows the pump curve behind it.
Real-time sensor data feeds the operator interface, where coke shows up as a pressure spike. The technician can stop and scrub that exact spot. Flow direction reverses from the station without hose changes.
Power is a Cummins QSL9 at 333 bhp, Tier 4 Final, the same engine on every pump in the fleet.`);
  }

  // =====================================================================
  // 11a. PUMP PERFORMANCE (was appendix)
  {
    const s = pres.addSlide();
    bg(s, C.white);
    chip(s, '04', 'Equipment & technology', false);
    title(s, 'TriMax pump performance', false);
    sub(s, 'Waterous CMU two-stage pump, one per pass: series-operation curve, as used for pigging', false);
    const ih = 4.5, iw = ih * 1000 / 1144, ix = 0.6, iy = 2.15;
    s.addShape(pres.shapes.RECTANGLE, { x: ix - 0.05, y: iy - 0.05, w: iw + 0.1, h: ih + 0.1, fill: { color: C.white }, line: { color: C.rule, width: 1 } });
    s.addImage({ path: IMG + 'pump_series.png', x: ix, y: iy, w: iw, h: ih });
    // effective-max band, 500–550 psi on the net-pressure axis
    const bx = ix + iw * 0.185, bw2 = iw * (0.845 - 0.185), by = iy + ih * 636 / 1144, bh2 = ih * 40 / 1144;
    s.addShape(pres.shapes.RECTANGLE, { x: bx, y: by, w: bw2, h: bh2, fill: { color: C.gold, transparency: 45 }, line: { color: 'B8860B', width: 1 } });
    s.addShape(pres.shapes.LINE, { x: ix + iw + 0.05, y: by + bh2 / 2, w: 0.45, h: 0, line: { color: 'B8860B', width: 1.5, beginArrowType: 'triangle' } });
    txt(s, [{ text: '500–550 psi', options: { bold: true, color: C.text, breakLine: true } }, { text: 'Effective maximum at the pig, after losses through our valves', options: { color: C.muted } }],
      { x: ix + iw + 0.6, y: by - 0.25, w: 3.2, h: 0.85, fontSize: 12, valign: 'top' });
    txt(s, [{ text: 'Reading the curve  ', options: { bold: true, color: C.text } }, { text: 'Each line is one engine speed; pressure falls as flow rises. Pigging runs well inside this envelope at 150 to 300 psi.', options: { color: C.muted } }],
      { x: ix + iw + 0.6, y: 5.55, w: 3.2, h: 1.2, fontSize: 11.5, valign: 'top' });
    txt(s, 'Manufacturer curve: Waterous Company, form F-2692', { x: ix, y: iy + ih + 0.1, w: 5, h: 0.25, fontSize: 9.5, italic: true, color: C.grey });
    const k = [['150–300', 'psi normal pigging'], ['500–550', 'psi effective max, after valve losses'], ['600', 'psi rated pump maximum']];
    k.forEach(([n, l], i) => {
      const y = 2.15 + i * 1.5;
      s.addShape(pres.shapes.RECTANGLE, { x: 8.55, y, w: 4.18, h: 1.3, fill: { color: i === 0 ? C.dark : C.light }, line: { color: i === 0 ? C.dark : C.light } });
      txt(s, n, { x: 8.8, y: y + 0.12, w: 3.7, h: 0.6, fontSize: 28, bold: true, color: i === 0 ? C.gold : C.text, valign: 'middle' });
      txt(s, l, { x: 8.8, y: y + 0.72, w: 3.7, h: 0.45, fontSize: 11.5, color: i === 0 ? C.white : C.muted, valign: 'top' });
    });
    footer(s, false);
    s.addNotes(`[~1 min] This is the manufacturer's curve behind the pressure bar on the last slide: the Waterous pump in series operation, which is how it runs for pigging (higher pressure, lower flow). Each line is one engine speed.
Normal pigging runs 150 to 300 psi, well inside the envelope. The pump is rated to 600 psi, but after losses through our valves the realistic ceiling at the pig is 500 to 550, the gold band. Above 500 the crew works an over-pressure checklist. That margin is what lets us push through a hard spot without running the pump at its limit.`);
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
    s.addNotes(`[~1 min] This is the operator screen from a TriMax station, the same software every pass runs on.
Walk the numbers: (1) the trend at the bottom plots pressure ahead of the pig, pressure behind it, and flow rate. When the pig meets coke you see the spike, and that's the "sensor data" indicator in our cleanliness verification. (2) Live GPM and psi. (3) Clean and effluent tank levels from guided-radar indicators. (4) Setpoint alarms; this one shows a clean-tank-low alert. (5) Pass completion and the pig run sheet and data sheet, so the pig log builds itself. (6) Each pass has its own station: left, center, right.
The takeaway for Valero: every decision on a pass is made from live data, and the record is automatic.`);
  }

  // =====================================================================
  // 12b. OPTIONAL CLOSED-LOOP FILTRATION
  {
    const s = pres.addSlide();
    bg(s, C.white);
    chip(s, '04', 'Equipment & technology', false);
    title(s, 'Optional closed-loop filtration', false);
    sub(s, 'Runs alongside pigging, independent of coil pressure', false);
    // loop diagram
    const nodes = [['TriMax\ndirty tank', 0.6], ['4×3 transfer\npump', 3.35], ['Filter\npress', 6.1], ['TriMax\nclean tank', 8.85]];
    const ny = 2.45, nw = 2.2, nh = 1.0;
    nodes.forEach(([t, x], i) => {
      const gold = i === 2;
      s.addShape(pres.shapes.RECTANGLE, { x, y: ny, w: nw, h: nh, fill: { color: gold ? C.gold : C.dark }, line: { color: gold ? C.gold : C.dark } });
      txt(s, t, { x, y: ny, w: nw, h: nh, fontSize: 14, bold: true, color: gold ? C.dark : C.white, align: 'center', valign: 'middle' });
      if (i < 3) s.addShape(pres.shapes.LINE, { x: x + nw + 0.05, y: ny + nh / 2, w: 0.45, h: 0, line: { color: C.grey, width: 2.5, endArrowType: 'triangle' } });
    });
    // return path
    s.addShape(pres.shapes.LINE, { x: 0.6 + nw / 2, y: ny + nh + 0.05, w: 0, h: 0.35, line: { color: C.grey, width: 2.5, beginArrowType: 'triangle' } });
    s.addShape(pres.shapes.LINE, { x: 0.6 + nw / 2, y: ny + nh + 0.4, w: 8.85 - 0.6, h: 0, line: { color: C.grey, width: 2.5 } });
    s.addShape(pres.shapes.LINE, { x: 8.85 + nw / 2, y: ny + nh + 0.05, w: 0, h: 0.35, line: { color: C.grey, width: 2.5 } });
    txt(s, 'Filtrate returns to the clean tank; pigging continues without interruption', { x: 2.2, y: ny + nh + 0.45, w: 6.8, h: 0.3, fontSize: 11, italic: true, color: C.muted, align: 'center' });
    // stats
    [['400 GPM', 'press capacity'], ['1,243 ft²', 'filtration area per press'], ['3', 'trailer-mounted presses in the fleet']].forEach(([n, l], i) => {
      const x = 0.6 + i * 3.55;
      txt(s, n, { x, y: 4.55, w: 3.3, h: 0.65, fontSize: 30, bold: true, color: C.text });
      txt(s, l, { x, y: 5.2, w: 3.3, h: 0.35, fontSize: 12, color: C.muted });
    });
    // benefits card
    const ben = ['Reduces fresh-water demand', 'Reduces wastewater volume', 'Coke fines captured as filter cake for disposal'];
    s.addShape(pres.shapes.RECTANGLE, { x: 0.6, y: 5.8, w: 12.13, h: 0.85, fill: { color: C.light }, line: { color: C.light } });
    ben.forEach((b, i) => {
      const x = 0.85 + i * 4.0;
      s.addShape(pres.shapes.OVAL, { x, y: 6.08, w: 0.28, h: 0.28, fill: { color: C.gold }, line: { color: C.gold } });
      txt(s, b, { x: x + 0.42, y: 5.95, w: 3.45, h: 0.55, fontSize: 12.5, bold: true, color: C.text, valign: 'middle' });
    });
    txt(s, 'Optional: priced separately', { x: 8.3, y: 4.62, w: 4.43, h: 0.5, fontSize: 11, italic: true, color: C.muted, align: 'right', valign: 'middle' });
    footer(s, false);
    s.addNotes(`[~1 min] Filtration is optional and priced separately. We ran it for Valero at Port Arthur.
Without filtration, supply water comes from a hydrant and the dirty tank discharges. With it, a frac tank feeds the loop: a 4×3 transfer pump moves dirty water from the TriMax through a trailer-mounted filter press, and the filtrate returns to the clean tank. It runs alongside pigging and doesn't affect coil pressure.
Each press handles 400 GPM across 1,243 square feet of filtration area, and we run three identical presses.
The benefits: far less fresh water drawn, far less wastewater to handle (thousands of gallons a shift), and the coke fines come out as filter cake for Valero's disposal. It's worth considering where water is limited or where the stainless coils call for controlled water quality.`);
  }

  // =====================================================================
  // 13. 4-POINT VERIFICATION
  {
    const s = pres.addSlide();
    bg(s, C.dark);
    chip(s, '05', 'Cleanliness verification & QA/QC', true);
    title(s, 'Verifying every pass is clean', true);
    sub(s, 'Four independent indicators, reviewed side by side with Valero', true);
    const cx = 6.67, cy = 4.55;
    s.addShape(pres.shapes.OVAL, { x: cx - 1.25, y: cy - 1.25, w: 2.5, h: 2.5, fill: { color: C.gold }, line: { color: C.gold } });
    txt(s, 'Joint\nsign-off\nper pass', { x: cx - 1.1, y: cy - 0.8, w: 2.2, h: 1.6, fontSize: 19, bold: true, color: C.dark, align: 'center', valign: 'middle' });
    const nodes = [
      ['FaChartLine', '1  Sensor data', 'Coke shows as a pressure spike; the tech stops and scrubs that exact spot', 0.6, 2.35, 'r'],
      ['FaWater', '2  Effluent returns', '"Black" in the return stream fades to nothing as the pass cleans', 8.95, 2.35, 'l'],
      ['PIGS', '3  Pig condition', 'Wear marks guide pig size and appendage choices', 0.6, 5.0, 'r'],
      ['FaCheckCircle', '4  Final gauge foam', 'Soft line-size (or slightly over) foam, witnessed by the Valero rep', 8.95, 5.0, 'l'],
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
    txt(s, 'Field-proven process: successful sign-offs from all of our clients and reliable first-attempt smart pig data.', { x: 0.6, y: 6.6, w: 12.1, h: 0.35, fontSize: 12, italic: true, color: C.gold, align: 'center' });
    s.addNotes(`[~2.5 min] How do we know a pass is clean? Four independent indicators, and the pass isn't called clean until all four agree.
1) Sensor data: live pressure data at the operator interface. Coke shows as a spike, and the technician can stop the pig and scrub that exact area.
2) Effluent: the technician watches the returns. The "black" (coke fines) in the stream fades to an unnoticeable amount as the pass cleans.
3) Pig condition: bi-directional runs leave tracking marks on the pigs (the photo shows real pigs after runs, with the wear visible). Those marks drive our size and appendage changes toward 100% removal.
4) Final gauge foam: when the interface, the water and the pigs all read clean, our shift leader invites the Valero rep to watch the final gauge foam run. It's line size or slightly over and soft enough to mark, groove or deform on any remaining coke. Valero reviews it with us and signs the pass off.
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
    sub(s, 'Governed by the USA DeBusk QA/QC manual', false);
    const cols = [
      ['FaClipboardList', 'Before', ['Pre-job walkdown with operations', 'Coil data checked against Valero records', 'JSA, permits and isolation confirmed', 'Pig progression staged by heater']],
      ['FaCogs', 'During', ['Daily report to one point of contact', 'Automated digital pig log per pass', 'Flow tests before and after at the same rate', 'JSA reviewed at every shift change']],
      ['FaBook', 'Close-out', ['Per-pass cleanliness sign-off', 'Final pig size recorded per pass', 'Job book delivered to Valero', 'Post-job review and lessons learned']],
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
    s.addNotes(`[~1 min] QA/QC runs through the whole job, not just the end.
Before: walkdown, coil data check, JSA/permits/isolation, pig progression staged by heater.
During: work is documented in the job book with daily reports, pig logs and JSAs. One point of contact manages the work flow and daily updates to Valero. Flow tests before and after at the same rate give an objective comparison.
Close-out: per-pass sign-off, final pig size recorded for each pass, the job book, and a post-job review. That record is what makes the next decoke on the same heater faster.
The full QA/QC manual is available on request.`);
  }

  // =====================================================================
  // 15. EMERGENCY RESPONSE
  {
    const s = pres.addSlide();
    bg(s, C.dark);
    s.addImage({ path: IMG + 'slot_shop.jpg', x: 0, y: 0, w: W, h: H });
    s.addShape(pres.shapes.RECTANGLE, { x: 0, y: 0, w: W, h: 2.1, fill: { color: '111111', transparency: 25 }, line: { color: '111111', transparency: 100 } });
    s.addImage({ path: IMG + 'fade_bottom_light.png', x: 0, y: 0, w: W, h: H });
    chip(s, '06', 'Emergency response', true);
    title(s, 'Responsive support for Texas City', true);
    locBadge(s, 'Based in Deer Park, TX', 2.0);
    sub(s, 'Our fleet stages at our Deer Park base, a short drive from Texas City', true);
    const st = [['24/7', 'Dispatch and account manager, any hour'], ['Same day', 'Response from Deer Park to Texas City'], ['6', 'TriMax units staged at Deer Park between jobs']];
    st.forEach(([n, l], i) => {
      const x = 0.6 + i * 4.1, y = 5.55;
      s.addShape(pres.shapes.RECTANGLE, { x, y, w: 3.9, h: 1.2, fill: { color: '151515', transparency: 15 }, line: { color: C.gold, width: 1.5 } });
      txt(s, n, { x: x + 0.2, y, w: 1.75, h: 1.2, fontSize: n.length > 5 ? 22 : 28, bold: true, color: C.gold, valign: 'middle' });
      txt(s, l, { x: x + 1.95, y, w: 1.85, h: 1.2, fontSize: 11.5, color: C.white, valign: 'middle' });
    });
    footer(s, true);
    s.addNotes(`[~1.5 min] Emergency response.
Our operating base is Deer Park. Every TriMax stages there when it isn't on a job, so Texas City is about as close to our equipment as a refinery gets.
Support is 24/7: dispatch and the account manager can be reached at any hour, with on-call supervisors and crews for nights, weekends and holidays.
Response is same day for Texas City when a unit is in the yard. If the fleet is committed, we'll tell you straight away when the next unit frees up.
The crew that has worked your heaters before is the crew that answers an unplanned call.
The photo: a TriMax and its support unit staged in the shop, fueled and ready to roll.`);
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
    s.addNotes(`[~1.5 min] Our Experience Modification Rate: 0.95 in 2024, 0.62 in 2025, 0.48 in 2026, roughly half the industry baseline and down 49% in two years. Active in ISNetworld with an A grade. No fatalities in the last three years. OSHA 300 logs are available on request.
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
      ['FaLock', 'Isolation first', "Valero's isolation and LOTO verified before any connection is made"],
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
Isolation: we don't connect until Valero's isolation and LOTO are verified.
Pressure: normal pigging is 150 to 300 psi; the pump is rated 600 but realistically tops out at 500 to 550 after valve losses, and above 500 psi the crew runs an over-pressure checklist.
Line of fire: every pig change bleeds to zero, and nobody stands in line with lids or hoses.
Hoses: tested and certified hard and flex pipe with whip checks on every connection.
PPE: FRC, hard hat, glasses or face shield, gloves, steel toes, hearing and respiratory protection as required. On stainless coils, no galvanized metal touches the tubes.
The pumper itself is engineered for safety too: retractable cam-actuated stairs, a composite work platform, LED lighting, and a self-contained design that prevents spills.
Full detail is in our safety manual and SSHASP, available on request.`);
  }

  // =====================================================================
  // 18. BEST PRACTICES & INNOVATION
  {
    const s = pres.addSlide();
    bg(s, C.dark);
    s.addImage({ path: IMG + 'slot_diff.jpg', x: 9.33, y: 0, w: 4.0, h: H });
    chip(s, '08', 'Capabilities', true);
    title(s, 'What sets USA DeBusk apart', true, { w: 8.4 });
    const cards = [
      ['FaIndustry', 'Self-performed scope', 'Pigging, decoking and hydroblasting with our own equipment and crews: one contractor, no subs'],
      ['FaCogs', 'Largest standardized fleet', '6 identical TriMax units, 18 engines, with a spare pump on board even on a 2-pass heater'],
      ['FaDotCircle', 'Widest pig selection', 'Engineered decoking pigs matched to each coil and each coke condition'],
      ['FaDatabase', 'Data-driven, shared', 'Durations built from recorded actuals; lessons learned reviewed with Valero after every job'],
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
    s.addNotes(`[~1.5 min] Four differentiators, backed by more than 200 years of combined experience on our team.
Self-performed: pigging, decoking and hydroblasting with in-house equipment and crews, so one contractor covers the full scope without subs.
Fleet: we run the largest triple-pass pigging fleet in the world, and it's standardized: six identical TriMax units, 18 engines. The TriMax runs up to three passes at once; on a 2-pass heater that third pump is an on-board spare, so a pump failure doesn't stop the job, and it can also drive a smart pig. We also offer closed-loop filtration and smart-pig support, so Valero deals with one contractor.
Pigs: the widest selection of engineered decoking pigs, matched to the coil and the coke (slide 6).
Data-driven and shared: our durations are built from recorded actuals, every job produces pig logs and a job report, and lessons learned are reviewed with the client after each job. Every return visit to a heater starts from that record, and Valero sits in that loop.`);
  }

  // =====================================================================
  // 19. VALERO REFERENCES MAP
  {
    const s = pres.addSlide();
    bg(s, C.dark);
    chip(s, '09', 'References & case study', true);
    title(s, 'Trusted across the Valero system', true);
    s.addImage({ path: IMG + 'valero_map.png', x: 0.4, y: 1.95, w: 7.2, h: 7.2 * 1200 / 1860 });
    txt(s, '14', { x: 7.9, y: 1.7, w: 1.4, h: 1.0, fontSize: 60, bold: true, color: C.gold, valign: 'middle' });
    txt(s, 'heaters cleaned at\n5 Valero refineries', { x: 9.3, y: 1.8, w: 3.45, h: 0.8, fontSize: 16, bold: true, color: C.white, valign: 'middle' });
    const refs = [
      ['Texas City, TX', 'H-57 coker heater, 2023 and 2024'],
      ['Port Arthur, TX', 'H-102A, H-102B, F-2000'],
      ['Three Rivers, TX', '100-H-1, 100-H-2, H-1102, H-1105, 440-H1'],
      ['Meraux, LA', 'VU-H-001, VU-H-002'],
      ['Wilmington, CA', '20H200, 20H2000, 31H3000'],
    ];
    refs.forEach(([site, heaters], i) => {
      const y = 2.95 + i * 0.68;
      s.addShape(pres.shapes.RECTANGLE, { x: 7.9, y, w: 0.06, h: 0.52, fill: { color: i === 0 ? C.white : C.gold }, line: { color: i === 0 ? C.white : C.gold } });
      txt(s, site, { x: 8.1, y: y - 0.02, w: 4.6, h: 0.28, fontSize: 13.5, bold: true, color: i === 0 ? C.gold : C.white });
      txt(s, heaters, { x: 8.1, y: y + 0.26, w: 4.6, h: 0.26, fontSize: 11.5, color: C.soft });
    });
    txt(s, 'Coker, vacuum, crude charge and reboiler service', { x: 7.9, y: 6.45, w: 4.85, h: 0.3, fontSize: 11.5, italic: true, color: C.gold });
    footer(s, true);
    s.addNotes(`[~1.5 min] Texas City isn't new to us: we pigged your H-57 coker heater in 2023 and again in 2024. Across Valero, that's 14 heaters at five refineries.
Port Arthur: the H-102A and H-102B vacuum heaters, which are the case study on the next slide, plus F-2000. Three Rivers: the 100-H-1 and 100-H-2 crude charge heaters, the H-1102 preflash reboiler, H-1105 and 440-H1. Meraux: both vacuum unit heaters. And on the West Coast, Wilmington's 20H200 and 20H2000 vacuum heaters and the 31H3000 coker feed heater.
That covers coker, vacuum, crude charge and reboiler service. Reference contacts at any of these sites are available on request.`);
  }

  // =====================================================================
  // 20. CASE STUDIES
  {
    const s = pres.addSlide();
    bg(s, C.white);
    chip(s, '09', 'References & case study', false);
    title(s, 'Valero case study & lessons learned', false);
    const cs = [
      ['Valero Port Arthur, TX: H-102A & H-102B', 'Vacuum heaters, March–April 2026',
        [['16', 'passes, 2 heaters'], ["18,496'", 'coil footage'], ['434', 'pigs run']],
        'Both 8-pass vacuum heaters pigged in triple mode, with filtration and smart pig inspection of every pass.',
        'Every pass signed clean and cleared by smart pig before rig-out. A mid-job TriMax swap rigged in within 2 hours, with no break in pigging.', 'Scope', 'Result'],
      ['Pass 6B: coke ring found by smart pig', 'Mixed-diameter vacuum pass, 3" to 8"',
        [['0.25"', 'thick coke ring'], ['24 h', 'dedicated pigging'], ['188 psi', 'flow-test reduction']],
        'Inspection found a circumferential coke ring at the inlet of a 5" tube, just before the step-up to 8".',
        'On mixed-diameter passes, stage pigs for every diameter and plan time at each step-up before the inspection run.', 'Challenge', 'Lesson learned'],
    ];
    cs.forEach(([h, d, stats, ch, lesson, chL, lesL], i) => {
      const x = 0.6 + i * 6.17, y = 1.95, w = 5.96;
      s.addShape(pres.shapes.RECTANGLE, { x, y, w, h: 4.8, fill: { color: C.light }, line: { color: C.light } });
      txt(s, h, { x: x + 0.35, y: y + 0.3, w: w - 0.7, h: 0.4, fontSize: 17, bold: true, color: C.text });
      txt(s, d, { x: x + 0.35, y: y + 0.7, w: w - 0.7, h: 0.3, fontSize: 12, color: C.muted });
      stats.forEach(([n, l], k) => {
        const sx = x + 0.35 + k * 1.8;
        txt(s, n, { x: sx, y: y + 1.2, w: 1.75, h: 0.65, fontSize: 28, bold: true, color: C.text });
        txt(s, l, { x: sx, y: y + 1.85, w: 1.75, h: 0.3, fontSize: 11, color: C.muted });
      });
      txt(s, [{ text: chL + '  ', options: { bold: true, color: C.text } }, { text: ch, options: { color: C.muted } }],
        { x: x + 0.35, y: y + 2.45, w: w - 0.7, h: 0.8, fontSize: 13, valign: 'top' });
      s.addShape(pres.shapes.RECTANGLE, { x: x + 0.35, y: y + 3.35, w: w - 0.7, h: 1.2, fill: { color: C.dark }, line: { color: C.dark } });
      txt(s, [{ text: lesL + '  ', options: { bold: true, color: C.gold } }, { text: lesson, options: { color: C.white } }],
        { x: x + 0.55, y: y + 3.45, w: w - 1.1, h: 1.0, fontSize: 13, valign: 'middle' });
    });
    footer(s, false);
    s.addNotes(`[~2 min] A Valero job from this year: the H-102A and H-102B vacuum heaters at Port Arthur, March into April 2026.
Two 8-pass heaters, 16 passes, about 18,500 feet of coil with diameters running from 3" up to 8" in the same pass. Heavy pitch and resid, concentrated in the 3" tubes. We ran in triple mode with filtration, and every pass was smart-pig inspected after cleaning. We went through 434 pigs, mostly in the 3" to 5" range.
Midway through, we swapped one TriMax for another. The new unit was rigged into three passes within two hours and pigging never stopped. That's the standardized fleet paying off.
The lesson is on pass 6B. The smart pig run found a quarter-inch coke ring at the inlet of the last 5" tube, right before the step-up to 8". It took about 24 hours of dedicated pigging to break, and inspection confirmed it clear before rig-out. Pass 6B's flow test came down 188 psi. What we took from it: on mixed-diameter passes, we stage pigs for every diameter and plan time at each step-up, so the inspection run confirms the result instead of finding work.`);
  }

  // =====================================================================
  // 21. WHY USA DEBUSK
  {
    const s = pres.addSlide();
    bg(s, C.dark);
    s.addImage({ path: IMG + 'slot_road.jpg', x: 0, y: 0, w: W, h: H });
    s.addImage({ path: IMG + 'fade_left.png', x: 0, y: 0, w: W, h: H });
    s.addImage({ path: IMG + 'fade_left.png', x: 0, y: 0, w: 10.5, h: H });
    chip(s, '10', 'Why USA DeBusk', true);
    title(s, 'Why USA DeBusk for Texas City', true, { w: 9.0, fontSize: 32 });
    const pts = [
      ['Proven at Valero', 'Your H-57 coker in 2023 and 2024, one of 14 Valero heaters we\'ve cleaned'],
      ['Close by', 'Fleet based in Deer Park, a short drive from Texas City'],
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
"We've pigged your H-57 coker twice, we know Valero's refineries, our fleet is down the road in Deer Park, the triple-pass rig carries its own spare pump, you sign off on every pass, and we do it safely."`);
  }

  // =====================================================================
  // 22. Q&A
  {
    const s = pres.addSlide();
    bg(s, C.dark);
    s.addShape(pres.shapes.RECTANGLE, { x: (W - 1.2) / 2, y: 4.3, w: 1.2, h: 0.06, fill: { color: C.gold }, line: { color: C.gold } });
    s.addImage({ path: IMG + 'logo_white.png', x: (W - 4.0) / 2, y: 1.6, w: 4.0, h: 4.0 * 101 / 674 });
    txt(s, 'Thank you', { x: 0.6, y: 2.6, w: 12.13, h: 1.0, fontSize: 48, bold: true, color: C.white, align: 'center' });
    txt(s, 'Questions & discussion', { x: 0.6, y: 3.55, w: 12.13, h: 0.5, fontSize: 22, color: C.gold, align: 'center' });
    txt(s, [
      { text: 'Jason Harman  |  Commercial Manager  |  jharman@usadebusk.com  |  (713) 839-5961' },
    ], { x: 0.6, y: 5.3, w: 12.13, h: 0.5, fontSize: 14, color: C.white, align: 'center' });
    s.addNotes(`[Q&A]
Likely questions and where the answer lives:
- "How do you handle a plugged pass?" Bi-directional flow and stepwise pig sizing (slides 4–6); planning from drawings (slide 7).
- "How long would our heater take?" Depends on footage, tube IDs and fouling. Offer to build a plan and quote from the heater's drawings.
- "How fast can you get here?" Slide 17: the fleet stages at Deer Park; same day when a unit is in the yard.
- "Have you worked at Valero before?" Slides 21–22: 14 heaters at five Valero refineries, including H-57 here in 2023 and 2024. Reference contacts on request.
- "Smart pig inspection?" The spare TriMax pump drives the inspection tool; Port Arthur had every pass inspected (slide 22).
- "Filtration?" Optional, priced per the Valero rate sheet.
- "Pump curves / pressure capability?" Slide 12 (Waterous CMU curves). Normal 150–300 psi; rated 600, 500–550 effective after valve losses.`);
  }

  await pres.writeFile({ fileName: __dirname + '/../Valero_TXC_Pigging_Capabilities.pptx' });
  console.log('written');
})();
