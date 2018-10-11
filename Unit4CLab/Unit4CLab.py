def draw7():

    for i in range (0,7):

        for x in range (0,7):

            print('*', end = '')

        print()

def StarsandStripes():

    for i in range (0,7):

        for x in range (0,7):
            if x == 1 or 3 or 5 or 7:
                print('*')
            if x == 2 or 4 or 6:
                print('-')

        print()

draw7()

StarsandStripes()
