import pandas as pd
import matplotlib.pyplot as plt
import os

DATA_PATH = "kaggle_data/items.csv"  

if not os.path.exists(DATA_PATH):
    raise FileNotFoundError(f"⚠️ Le fichier '{DATA_PATH}' est introuvable. Vérifie le chemin.")

data = pd.read_csv(DATA_PATH)
print(data.head())

print("\n--- Informations générales ---")
print(data.info())

print("\n--- Statistiques numériques ---")
print(data.describe())

# Si le dataset contient des valeurs manquantes
missing = data.isnull().sum()
print("\n--- Valeurs manquantes ---")
print(missing[missing > 0])

