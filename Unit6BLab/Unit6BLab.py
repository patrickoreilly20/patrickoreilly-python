import Unit6BList as dict

x = input("What month is your birthmonth - ")

y = int(input("What is the day of your birth  - "))

z = int(input('What are the last two digits of your birthyear - '))
for b in dict.weekends :

    if b==x :

        for c in dict.weekends[b] :

            if c==y :

                print("Awesome, your birthday is on a weekend!")

                dict.d = 0
if dict.d==1 :

    print("Sad times, your birthday is on a weekday")

if x == 'january':
    print('01/',end='')

if x == 'february':
    print('02/',end='')

if x == 'march':
    print('03/',end='')

if x == 'april':
    print('04/',end='')

if x == 'may':
    print('05/',end='')

if x == 'june':
    print('06/',end='')

if x == 'july':
    print('07/',end='')

if x == 'august':
    print('08/',end='')

if x == 'september':
    print('09/',end='')

if x == 'october':
    print('10/',end='')

if x == 'november':
    print('11/', end='')

if x == 'december':
    print('12/', end='')

else: print()

print(str(x) + ' ' + str(y) + ' ' + str(z))
