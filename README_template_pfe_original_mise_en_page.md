# Template PFE ENCG – Mise en page originale conservée

Ce pack contient un template DOCX créé à partir du rapport de stage original.

## Fichiers
- `template_pfe_encg_original_mise_en_page.docx` : modèle Word avec la page de garde et la mise en page d’origine.
- `mapping_pfe_encg_original_mise_en_page.json` : liste des variables à remplir.
- `exemple_payload_pfe_original_mise_en_page.json` : exemple de JSON compatible.
- `fill_template_docxtpl_pfe.py` : script Python de remplissage via `docxtpl`.

## Utilisation rapide
```bash
pip install docxtpl
python fill_template_docxtpl_pfe.py template_pfe_encg_original_mise_en_page.docx exemple_payload_pfe_original_mise_en_page.json rapport_final.docx
```

Après ouverture dans Word : clic droit sur la table des matières > Mettre à jour les champs.
