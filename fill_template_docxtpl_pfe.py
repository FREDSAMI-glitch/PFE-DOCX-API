import sys, json
from docxtpl import DocxTemplate

if len(sys.argv) != 4:
    print('Usage: python fill_template_docxtpl_pfe.py template.docx payload.json output.docx')
    sys.exit(1)

template_path, payload_path, output_path = sys.argv[1], sys.argv[2], sys.argv[3]
with open(payload_path, 'r', encoding='utf-8') as f:
    context = json.load(f)

doc = DocxTemplate(template_path)
doc.render(context)
doc.save(output_path)
print('DOCX généré :', output_path)
