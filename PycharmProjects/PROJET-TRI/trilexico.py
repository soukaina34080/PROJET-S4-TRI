import csv
import random
import string
import time
from string import ascii_letters

def sortLexo(nbElem): 
    start_time = time.time() # enregistre le temps de départ
    listwords = ["".join(random.choice(ascii_letters) # choisi une lettre au hasard (le join va permettre de créer un mot(joindre les lettres))
                         for j in range(random.randint(2,10)) ) # nombre de lettres dans le mot (choisi au hasard)
                 for i in range(nbElem) ] # nombre de mots dans la liste à trier
  
    # tri les mots de la liste dans l'odre lexicographique
    listwords.sort() 
    
    # affiche la liste de mots triés
    print(listwords) 
    
    tempsEc = time.time() - start_time; # calcul du temps écoulé (temps actuel moins le temps de départ)
    print("Temps d'execution : %s secondes" % (tempsEc)) # affiche à l'écran le temps écoulé
    
    # ouvre le fichier dans lequel on va enregistrer le temps qui va être nommé après le nombre d'éléments dans la liste
    f = open( '%dtrilexico.txt' %nbElem, 'a' ) 
    f.write( str(tempsEc) + '\n' )
    f.close() 
    
    # calcul de la moyenne du temps d'exécution de l'algo
    somme = 0
    moyenne = 0
    nbLigne = 0
    cr = csv.reader(open("%dtrilexico.csv" %nbElem, "r")) # on ouvre le fichier où sont enregistrer les temps
    for r in cr: #r = colonne
        somme  += float(r[0]) # on somme chacun des temps
        nbLigne += 1 # on compte le nombre de lignes (= nombre de temps enregistrés)
    print("Somme temps : %s" % somme)
    moyenne = somme / nbLigne # calcul du temps moyen
    print("Moyenne : %s" % moyenne) # affiche le temps moyen
  
    
    # stockage du temps moyen dans un fichier
    moy = open('%dmoytrilexico.csv' % nbElem, 'w')
    moy.write(str(moyenne) + '\n')
    moy.close()
     

if __name__ == '__main__': 


    
    sortLexo(10) # appel de l'algorithme
