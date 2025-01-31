#!/usr/bin/env python
# coding: utf-8

# In[8]:


import pandas as pd
import os

input_folder = r"input"
output_folder = r"output"

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Vérifier que le dossier existe
if not os.path.exists(input_folder):
    print("Le dossier n'existe pas.")
    open('error.txt', 'w').write("Le dossier `"+input_folder+"` n'existe pas.")
    input("Appuyez sur une touche pour quitter...")

# Récupérer les fichiers CSV dans le dossier
files = os.listdir(input_folder)

# Lire les fichiers CSV dans le dossier et les concaténer
df = pd.concat([pd.read_csv(input_folder + "/" + file) for file in files if file.endswith(".csv")])

# Detect duplicated lines from the first column of the input file (we don't now how the columns are named)
duplicated_lines = df[df.duplicated(subset=df.columns[0], keep=False)]

with open(output_folder + "/rapport.txt", "w") as f:
    f.write("Rapport de détection de doublons\n")
    f.write("Nombre de lignes : " + str(len(df)) + "\n")
    f.write("--------------------------\n")
    f.write("Liste des doublons :\n")
    for index, row in duplicated_lines.iterrows():
        f.write(str(index) + " : " + str(row.values[0]) + "\n")
        
print("Rapport généré avec succès.")
input("Appuyez sur une touche pour quitter...")

