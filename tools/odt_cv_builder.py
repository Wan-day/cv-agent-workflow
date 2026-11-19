# Written by an AI agent (Claude Code) during a CV-tailoring session, reviewed by the repo owner.
# Builds a tailored CV .odt from a Markdown cv.md, reusing the paragraph styles of a base CV .odt.
# Usage: python3 odt_cv_builder.py <unzipped base CV>/content.xml jobs/<slug>/cv.md > content.xml
#        then put content.xml back into the unzipped .odt and re-zip (mimetype first, uncompressed).
import sys
from xml.sax.saxutils import escape as E
src, md = sys.argv[1], sys.argv[2]
x = open(src, encoding='utf-8').read()
start = x.index('<text:h text:style-name="P9" text:outline-level="1">SUMMARY')
end = x.index('</office:text>')
out = []
first_list = [True]
def H(t): out.append(f'<text:h text:style-name="P9" text:outline-level="1">{E(t)}</text:h>')
def P(style, t, span='T6'): out.append(f'<text:p text:style-name="{style}"><text:span text:style-name="{span}">{E(t)}</text:span></text:p>')
def label(style, lab, t): out.append(f'<text:p text:style-name="{style}"><text:span text:style-name="T5">{E(lab)} </text:span><text:span text:style-name="T6">{E(t)}</text:span></text:p>')
def title(t, right=None, link=None):
    r = ''
    if link: r = f'<text:tab/><text:a xlink:type="simple" xlink:href="https://{link}" text:style-name="ListLabel_20_13" text:visited-style-name="ListLabel_20_13"><text:span text:style-name="T3">{E(link)}</text:span></text:a>'
    elif right: r = f'<text:tab/><text:span text:style-name="T2">{E(right)}</text:span>'
    out.append(f'<text:p text:style-name="P10"><text:span text:style-name="T8">{E(t)}</text:span>{r}</text:p>')
def bullets(items):
    if first_list[0]:
        o = '<text:list text:style-name="WWNum2">'; first = ' text:start-value="1"'; first_list[0] = False
    else:
        o = '<text:list text:continue-numbering="true" text:style-name="WWNum2">'; first = ''
    for i, it in enumerate(items):
        o += f'<text:list-item{first if i == 0 else ""}><text:p text:style-name="P11"><text:span text:style-name="T6">{E(it)}</text:span></text:p></text:list-item>'
    out.append(o + '</text:list>')
def stack(t, lab='Stack: '): out.append(f'<text:p text:style-name="P12"><text:span text:style-name="T5">{lab}</text:span><text:span text:style-name="T9">{E(t)}</text:span></text:p>')

# parse the cv.md body (after the header) into blocks
lines = open(md, encoding='utf-8').read().split('\n')
section = None; pend = []
def flush():
    if pend: bullets(pend[:]); pend.clear()
skills = []
for ln in lines:
    s = ln.strip()
    if s.startswith('## '):
        flush()
        if section in ('SKILLS','DOVEDNOSTI'):
            for i, (l, t) in enumerate(skills):
                label('P7' if i == len(skills) - 1 else 'P6', l, t)
            pass
        section = s[3:]; H(section); continue
    if section is None or not s or s.startswith('<!--'): continue
    if section in ('SUMMARY','PROFIL'): P('P5', s, 'T6'); continue
    if section in ('SKILLS','DOVEDNOSTI'):
        b = s.lstrip('- ').split('**')
        skills.append((b[1], b[2].strip())); continue
    if s.startswith('**'):
        flush()
        name, rest = s[2:].split('**', 1)
        rest = rest.strip().lstrip('·').strip()
        if rest.startswith('github.com'): title(name, link=rest)
        else: title(name, right=rest or None)
        continue
    if s.startswith('- '): pend.append(s[2:]); continue
    flush()
    if s.startswith('Stack: '): stack(s[7:]); continue
    if s.startswith('Technologie: '): stack(s[13:], 'Technologie: '); continue
    P('P13', s)
flush()
sys.stdout.write(x[:start] + ''.join(out) + x[end:])
