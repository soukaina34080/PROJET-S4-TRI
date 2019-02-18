#!/usr/bin/env python
import random
import time


def radixSort(nbElem):
    start_time = time.time()
    list_vals = random.sample(range(1000),nbElem)
    RADIX = 10
    maxLength = False
    tmp = -1
    placement = 1

    while not maxLength:
        maxLength = True
        buckets = [list() for _ in range( RADIX )]

        for i in list_vals:
            tmp = i // placement
            buckets[tmp % RADIX].append( i )
            if maxLength and tmp > 0:
                maxLength = False

        a = 0

        for b in range( RADIX ):
            buck = buckets[b]
            for i in buck:
                list_vals[a] = i
                a += 1

        placement *= RADIX
    print(list_vals);
    tempsEc = time.time() - start_time;
    print("Temps d'execution : %s secondes" % (tempsEc))
    
    
    f = open( '%dtribase.txt' %nbElem, 'a' )
    f.write( str(tempsEc) + '\n' )
    f.close() 
     



def main():
    radixSort(25);

if __name__ == "__main__":

    main()