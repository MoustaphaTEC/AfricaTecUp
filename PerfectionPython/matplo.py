import matplotlib.pyplot as plt  # nous créons des graphiques grâce à l'objet matplotlib.pyplot
import seaborn as sns  # afin de rendre les graphiques un peu plus beaux

ages = [25, 65, 26, 26, 46, 37, 36, 36, 28, 28, 57, 37, 48, 48, 37, 28, 60,
        25, 65, 46, 26, 46, 37, 36, 37, 29, 58, 47, 47, 48, 48, 47, 48, 60]
fig, ax = plt.subplots()  # renvoie un tuple contenant deux objets, que l'on nomme communément fig et ax
ax.axis("equal")
ax.hist(ages)  # ax, il représente notre unique graphique. ax.hist() : affiche un histogramme,
plt.title("Histogramme d'Ages")
# plt.show()  # Pour afficher la fenêtre

fig, ax = plt.subplots()
ax.axis("equal")
ax.pie([24, 18],
       labels=["Femmes", "Hommes"],
       autopct="%1.1f pourcents")
plt.title("Un superbe graphique")
plt.show()
