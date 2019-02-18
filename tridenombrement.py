import csv
import random
import time
from array import array


def counting_sort(nbElem):
    start_time = time.time()
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
            # affichage avant après
    print(list_vals);
    print(list_sorted);

    tempsEc = time.time() - start_time;
    print("Temps d'execution : %s secondes" % (tempsEc))

    f = open('%dtridenombrement.csv' % nbElem, 'a')
    f.write(str(tempsEc) + '\n')
    f.close()

    somme = 0
    cr = csv.reader(open("%dtridenombrement.csv" %nbElem, "r"))
    for r in cr: #r = colone
        somme  += float(r[0])
    print("Somme temps : %s" % somme)


        # moy = 0
        # moy = somme / len(cr.readlines())
        # print(moy)


def main():
    counting_sort(15);


main()


