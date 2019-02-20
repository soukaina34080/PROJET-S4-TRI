import csv
import random
import time
import matplotlib.pyplot as plt
import os
import getpass


def counting_sort(nbElem):
    #debut timer
    start_time = time.time()
    # mise en place d'une liste de nbElem de 0 à 1000
    list_vals = random.sample(range(1000), nbElem)

    liste = []
    moyenne = 0

    #  récup valeur max de la liste aléatoire
    max_val = max(list_vals);

    list_counts = [];
    list_sorted = [];
    # initialise chaque élément à 0
    list_counts = [0 for i in range(0, max_val + 1)];

    # fréquence de chaque elemt du tableau
    for i in range(0, len(list_vals)):
        list_counts[list_vals[i]] += 1;

        # ajoute les elements triés selon la fréquence
    for i in range(0, max_val + 1):
        while (list_counts[i] > 0):
            list_sorted.append(i);
            list_counts[i] -= 1;

    # affichage avant après tri
    print(list_vals);
    print(list_sorted);

    # calcul temps écoulé
    tempsEc = time.time() - start_time;
    print("Temps d'execution : %s secondes" % (tempsEc))

    # écrit le temps écoulé dans le fichier [nbElem]tridenombrement.csv
    savepathTemps = '/home/' + getpass.getuser() + '/PycharmProjects/PROJET-TRI/temps'
    completePathTemps = os.path.join(savepathTemps, '%dtridenombrement.csv ' % nbElem)
    f = open(completePathTemps, 'a')
    f.write(str(tempsEc) + '\n')
    f.close()

    # calcul de la moyenne à l'aide des variable : somme, moyenne, nbLigne
    somme = 0
    moyenne = 0
    nbLigne = 0

    # on ouvre le fichier contenant les temps en lecture
    cr = csv.reader(open(completePathTemps, "r"))

    # pour chaque élément de la colonne r, on additionne les valeur et on
    # incrémente le nbLigne afin de calculer la moyenne
    for r in cr:  # r = colone
        somme += float(r[0])
        nbLigne += 1
    # print("Somme temps : %s" % somme)
    moyenne = somme / nbLigne
    print("Moyenne : %s" % moyenne)
    print("Nb valeur : %s " % nbLigne)

    # on enregistre la moyenne obtenu dans le fichier moytridenombrement.txt
    savepathMoy = '/home/' + getpass.getuser() + '/PycharmProjects/PROJET-TRI/moy'
    completePathMoy = os.path.join(savepathMoy, 'moytridenombrement.txt')
    moy = open(completePathMoy, 'a')
    moy.write(str(moyenne) + ',' + str(nbElem) + '\n')
    moy.close()


def courbe():
    # on affiche la courbe des moyennes selon le nbElem
    x = []
    y = []

    savepathMoy = '/home/' + getpass.getuser() + 'PycharmProjects/PROJET-TRI/moy'
    completePathMoy = os.path.join(savepathMoy, 'moytridenombrement.txt')
    # on ouvre le fichier contenant les moyennes selon le nbElem
    with open(completePathMoy, 'r') as csvfile:
        # on délimite la séparation entre la moyenne et le nbElem par une virgule
        plots = csv.reader(csvfile, delimiter=',')
        # on attribut les valeurs du nbElem à x et de la moyenne à y
        for row in plots:
            x.append(float(row[1]))
            y.append(float(row[0]))
    # on dessine la courbe
    plt.plot(x, y, label='Denombrement')
    plt.xlabel('nbElem')
    plt.ylabel('Temps')
    plt.title('Courbe tri')
    plt.legend()
    plt.show()

    # on efface les moyenne afin d'afficher une nouvelle courbe
    # avec les nouvelles valeurs
    open(completePathMoy, "w").close()


def main():
    counting_sort(10);
    counting_sort(15);
    counting_sort(20);
    counting_sort(25);
    counting_sort(30);
    counting_sort(35);

    courbe();


main()
