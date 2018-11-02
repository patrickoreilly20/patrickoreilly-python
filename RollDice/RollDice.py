from random import *

def dice () :

    loop = 'yes'

    times = 0

    while loop=='yes' :

        times = times + 1

        y = randNum ()

        print(diceSide(y))

        print ("The roll is - " + str(y))

        loop = input ("Want to roll again? (yes/no) - ")

        print ("You have played " + str(times) + " times.")


def randNum () :

    x = randint(1,6)
    #print(x)

    #input()

    return (x)

def diceSide (randnum) :

    a = ' ------- '

    if randnum==1 or randnum==2 :

        b = '|       |'

    elif randnum==3 :

        b = '|   *   |'

    elif randnum==4 or randnum==5 or randnum==6 :

        b = '| *  *  |'


    if randnum==1 or randnum==3 or randnum==5 :

        c = '|   *   |'

    elif randnum==4 :

        c = '|       |'

    elif randnum==2 or randnum==6 :

        c = '| *  *  |'

    if randnum==1 or randnum==2 :

        d = '|       |'

    elif randnum==3 :

        d = '|   *   |'

    elif randnum==4 or randnum==5 or randnum==6 :

        d = c = '| *  *  |'

    e = ' ------- '

    return(a + "\n" + b + "\n" + c + "\n" + d + "\n" + e)




dice ()

