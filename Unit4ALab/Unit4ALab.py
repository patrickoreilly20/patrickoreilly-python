
def main():

    strWord = input('Input your word here - ')

    #print(strWord)

    print(deVowel(strWord))

def deVowel(strWord):

    noVowel = ''

    for x in strWord:

        if x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u':

            y = 'p'

        else:

            noVowel = noVowel + x

    return (noVowel)

main()
