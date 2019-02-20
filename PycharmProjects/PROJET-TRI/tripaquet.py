import time
import random
import math
import csv


def bucketSort(nbElem):
    array = random.sample(range(1000), nbElem) #initialise tableau d'entier
    if len(array) == 0:
        return array
    bucketSize= 10

    # Determine minimum and maximum values
    minValue = array[0]
    maxValue = array[0]
    for i in range(1, len(array)):
        if array[i] < minValue:
            minValue = array[i]
        elif array[i] > maxValue:
            maxValue = array[i]

    # Initialize buckets
    bucketCount = math.floor((maxValue - minValue) / bucketSize) + 1
    buckets = []
    for i in range(0, int(bucketCount)):
        buckets.append([])

    # Distribute input array values into buckets
    for i in range(0, len(array)):
        buckets[math.floor((array[i] - minValue) / bucketSize)].append(array[i])

    # Sort buckets and place back into input array
    array = []
    for i in range(0, len(buckets)):
        insertion_sort.sort(buckets[i])
        for j in range(0, len(buckets[i])):
            array.append(buckets[i][j])

    return array

    #calcul de la moyenne du temps d'exécution de l'algo
    somme = 0
    moyenne = 0
    nbLigne = 0
    cr = csv.reader(open("%dtripaquet.csv" %nbElem, "r"))
    for r in cr: #r = colonne
        somme  += float(r[0])
        nbLigne += 1
    print("Somme temps : %s" % somme)
    moyenne = somme / nbLigne
    print("Moyenne : %s" % moyenne)
    print("Nb valeur : %s " % nbLigne)
    
    #stockage du temps moyen dans un fichier
    moy = open('%dmoytripaquet.csv' % nbElem, 'w')
    moy.write(str(moyenne) + '\n')
    moy.close()
    
def main():
    
    bucketSort(15);


main()
