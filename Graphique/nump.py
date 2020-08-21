import numpy as np
import pandas as pd

# famille_panda = [
#     np.array([100, 5  , 20, 80]), # maman panda
#     np.array([50 , 2.5, 10, 40]), # bébé panda
#     np.array([110, 6  , 22, 80]), # papa panda
# ]


famille_panda = [
    [100, 5, 20, 80],  # maman panda
    [50, 2.5, 10, 40],  # bébé panda
    [110, 6, 22, 80],  # papa panda
]

famille_panda_numpy = np.array(famille_panda)
print(famille_panda_numpy)

# famille_panda_df = pd.DataFrame(famille_panda)

famille_panda_df = pd.DataFrame(famille_panda_numpy, index=['maman', 'bebe', 'papa'],
                                columns=['pattes', 'poil', 'queue', 'ventre'])
print(famille_panda_df)

# for ligne in famille_panda_df.iterrows():
#     index_ligne = ligne[0]
#     contenu_ligne = ligne[1]
#     print("Voici le panda %s :" % index_ligne)
#     print(contenu_ligne)
#     print("--------------------")
print()
print(famille_panda_df.iloc[2])  # Avec iloc(), indexation positionnelle
print()
print(famille_panda_df.loc["papa"])  # Avec loc(), indexation par label
print()
masque = famille_panda_df["ventre"] == 80
pandas_80 = famille_panda_df[masque]
print(pandas_80)
print(famille_panda_df[~masque])
quelques_pandas = pd.DataFrame([[105, 4, 19, 80], [100, 5, 20, 80]],  # deux nouveaux pandas
                               columns=famille_panda_df.columns)  # même colonnes que famille_panda_df
tous_les_pandas = famille_panda_df.append(quelques_pandas)
print(tous_les_pandas)
print(tous_les_pandas.drop_duplicates())