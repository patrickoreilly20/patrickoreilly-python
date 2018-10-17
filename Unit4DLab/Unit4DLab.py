def main():

    shoppingCart = [['tooth paste', 'q-tips', 'milk'], ['milk', 'candy', 'apples'], ['paper', 'pencils', 'q-tips']]

    #print (shoppingCart)

    allinOneList = allInOne(shoppingCart)

def allInOne(myShoppingCart):

    print(myShoppingCart)

    listtot=[]

    for i in myShoppingCart :

            for items in i:

                listtot.append(items)

    print(listtot)

    countQtipstotal = countQtips(listtot)

def countQtips(totalQtips):

    print(totalQtips)







main()
