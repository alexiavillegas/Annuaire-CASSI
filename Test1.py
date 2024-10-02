import pandas as pd
import pdfplumber

#Liste pour stocker le texte extrait
data = []

#Chemin vers l'annuaire (PDF)
pdf_path = '/Users/alexia/Desktop/testExtraction/annuaire1.pdf'

#J'ouvrir et j'extrait le texte du PDF
with pdfplumber.open(pdf_path) as pdf:
    for page in pdf.pages:
        text = page.extract_text()
        if text:  # Si du texte est extrait
            lines = text.split('\n')  #retour à la ligne => séparateur
            data.extend(lines)

#Je convertie la liste de données en DataFrame 
df = pd.DataFrame(data, columns=["données annuaire 1"])

#J'enregistre les données dans un fichier Excel
excel_path = '/Users/alexia/Desktop/testExtraction/donnees_extraites.xlsx'
df.to_excel(excel_path, index=False)

print(f"Les données ont bien été exportées dans {excel_path} !")