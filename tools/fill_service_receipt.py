"""Fill the DEBUSK service receipt template from a JSON of field values.

Usage: python tools/fill_service_receipt.py <data.json> <out.pdf>

Keys are the template's AcroForm field names (receipt_no, date, shift_day, rig_out,
operator_1, shift_summary_1, ...); an unknown key aborts. Checkboxes take true/false.
Warns when a value is too wide for its field, since viewers silently shrink it.
"""
import json
import sys

import fitz

TEMPLATE = r"C:\Users\Jwuts\obsidian-work\templates\DEBUSK_Service_Receipt_TEMPLATE.pdf"

data = json.load(open(sys.argv[1], encoding="utf-8"))
out = sys.argv[2]

doc = fitz.open(TEMPLATE)
page = doc[0]
known = {w.field_name for w in page.widgets()}
unknown = [k for k in data if k not in known]
if unknown:
    sys.exit(f"ERROR unknown field(s): {unknown}")

HELV = fitz.Font("helv")
filled = 0
overflow = []
for w in page.widgets():
    if w.field_name not in data:
        continue
    v = data[w.field_name]
    if w.field_type == fitz.PDF_WIDGET_TYPE_CHECKBOX:
        w.field_value = bool(v)
    else:
        if v == "":
            continue
        # A viewer silently SHRINKS text that will not fit, which is how the
        # Materials/Equipment line came out tiny on 8426-8428. Catch it here.
        size = w.text_fontsize or 10.5
        need = HELV.text_length(str(v), size)
        avail = w.rect.width - 3
        if need > avail:
            overflow.append(
                f"  {w.field_name}: needs {need:.0f}pt, field is {avail:.0f}pt "
                f"— will shrink. Split it across a continuation line."
            )
        w.field_value = str(v)
    w.update()
    filled += 1

if overflow:
    print("OVERFLOW — text will render smaller than 10.5pt:")
    print("\n".join(overflow))

doc.save(out)
print(f"wrote {out} — {filled} fields filled")
