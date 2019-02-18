import random
import string
import time
from string import ascii_letters

def sortLexo(nbElem): 
    start_time = time.time() #enregistre le temps de début
    listwords = ["".join(random.choice(ascii_letters) 
                         for j in range(random.randint(2,10)) ) #nb lettre mot
                 for i in range(nbElem) ] #nb mot
  
    # tri chaine de carac
    listwords.sort() 

    # affiche les mots dans l'ordre alphabetique
    # for i in listwords: 
    #    print( i )  
        
    
    print(listwords) #affiche la liste de mots triés
    
    tempsEc = time.time() - start_time; #temps écoulé
    print("Temps d'execution : %s secondes" % (tempsEc))
    
    
    f = open( '%dtrilexico.txt' %nbElem, 'a' ) #ouvre le fichier dans lequel on va enregistrer le temps
    f.write( str(tempsEc) + '\n' )
    f.close() 
     

if __name__ == '__main__': 


    
    sortLexo(10)
