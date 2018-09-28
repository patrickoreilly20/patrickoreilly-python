def main() :

    gradeYear = input('What year are you in school - ')

    print(gradeYear)

    strGrade = getgrade(gradeYear)

    print (strGrade)

    avgGrade = [92.6,92.8,95.6,98.1]

    theAvggrade = avggpa(avgGrade,len(avgGrade))

    strPercent = lettergrade(theAvggrade)

    print(strPercent)

    if strPercent == 'You have an A' or strPercent == 'You have a B' or strPercent == 'You have a C':
        print('You are passing')
    else:
        print('You are failing')



def getgrade(gradeYear):



        if gradeYear == '9':

            return('freshman')

        elif gradeYear == '10':

            return('sophmore')

        elif gradeYear == '11':

            return('junior')

        elif gradeYear == '12':

            return('senior')

        else:

            return('You are not in highschool')


def avggpa(mylist,num) :

        print(mylist)
        print(num)

        x = mylist[0] + mylist[1] + mylist[2] + mylist[3]

        y = x / 4

        return y

def lettergrade(percentgrade):

        if percentgrade >= 92.5:

            return('You have an A')

        elif percentgrade >= 88:

            return('You have a B')

        elif percentgrade >= 78:

            return('You have a C')

        elif percentgrade >= 72:

            return ('You have a D')

        elif percentgrade >= 65:

            return ('You have a F')

        else:

            return('Do you even show up to class?')



main()

