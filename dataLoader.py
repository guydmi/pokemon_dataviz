import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

from IPython.display import display

import os

os.listdir("datasets")
os.listdir("pokemap")

pokemon = pd.read_csv("datasets/pokemon1.csv")

places = pd.read_csv("datasets/places1.csv", sep = ";", on_bad_lines='skip')



for pokemonList in places['Pokemons']:
    pokemons = [name.strip().strip("'") for name in pokemonList[1:-1].split(",")]
    for pok in pokemons:
        if not (pok in set(pokemon['name'])):
            print(pok + ";" + pokemonList)



def display_dataframe_infos(df):
    print("General information")
    print(df.info())

    print("\n\nSummary statistics")
    print(df.describe())

    print("\n\nFirst 5 rows")
    print(df.head())






