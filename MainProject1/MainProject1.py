def main() :

    gradeYear = input('What year are you in school - ')

    print(gradeYear)

    strGrade = getgrade(gradeYear)

    print (strGrade)

    print (avggpa())

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


def avggpa() :

        avgGrade = [92.6,92.8,95.6,98.1]

        x = avgGrade[0] + avgGrade[1] + avgGrade[2] + avgGrade[3]

        y = x / 4

        return y

def lettergrade()

main()
