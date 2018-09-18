def schoolSub() :
    print('I go to Bellarmine')
    print('My favorite Subject is Python')

schoolSub()

def schoolLen() :
    years = input('What year are you in school? - ')
    yearsSchool = (int(years) - 1)
    print('you have been in school ' +str(yearsSchool) + ' years')

schoolLen()


def homeBase() :
    home = input ('What city are you from - ')
    schoolYears = input ('How  many years have you been in school - ')
    print ('You are from ' +str(home))
    print ('You have been in school for ' +str(schoolYears) + ' years')

homeBase()

from random import *

def randomNumber():
    x = input('What is your start value - ')
    y = input('What is your ending value - ')
    myNumber = randint(int(x) , int(y))
    print(str(myNumber) + ' a random number between ' +str(x) + ' and ' +str(y))

randomNumber()

def boxArea():
    x = input('What is the length of your box in centimeters - ')
    y = input('what is the width of your box in centimeters - ')
    area = int(x) * int(y)
    print('The area of your box is ' +str(area) + ' centimeters^2')

boxArea()

def boxPerim():
    x = input('What is the length of your box in centimeters - ')
    y = input('What is the width of your box in centimeters - ')
    perim = int(x) + int(x) + int(y) + int(y)
    return(perim)

boxPerim()
