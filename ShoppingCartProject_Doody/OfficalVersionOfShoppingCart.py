class Products:

    def __init__(self,name, price):
        self.__name = name
        self.__price = price

    def loadListData(self, fileName):
        items = []
        products = open(fileName, 'r')
        for line in products:
            items.append(line)
        return items

    def getitemName(self):
        return self.__name

    def getitemPrice(self):
        return self.__price

    def display(self):
        print(self.__name, '\t',  '$' + str(self.__price))

class CartItem():

    def __init__(self,product, quantity):
        self.__product = product
        self.__quantity = quantity

    def getProduct(self):
        return self.__product

    def getQuantity(self):
        return self.__quantity

    def __str__(self):
         return('Your cart has : {} {} {} '.format(self.__quantity,
                                                   " of " + self.__product.getitemName(),
                                                   "for  $" + str(self.__product.getitemPrice())))

class ShoppingCart:

    salesTax = .07
    def __init__(self):
        self.__cartItemList = []

    def __str__(self):
        cartString = ""

        for cartItem in self.__cartItemList:
            cartString += str(cartItem) + '\n'
        return cartString

    def addCartItem(self,inventory):
        MovieNumber = int(input("Please enter the movie you would like to add to your cart:"))

        if( 5 >= MovieNumber >= 0):
            quantity = int(input("Please enter the Amount you want: "))
            cartItem = CartItem(inventory[MovieNumber - 1], quantity)
            self.__cartItemList.append(cartItem)

        else:
             print("Please enter a number between 1-5")

    def removeCartItem(self):

        if len(self.__cartItemList) == 0:
            print("You have nothing in your cart")
        else:
            self.printCart()
            itemRemoved = int(input("Please enter the item number you would like to remove: "))
            if(itemRemoved <= len(self.__cartItemList)):
                del self.__cartItemList[itemRemoved - 1]
            else:
                print("Please enter a valid number.")


    def printCart(self):
        if (len(self.__cartItemList) == 0):
            print('You have nothing in your cart')
        else:
            count = 1
            for item in self.__cartItemList:
                print('#', count, end=' ')
                print(item)
                count += 1

    def calculateTotal(self): # calculate total
        subtotal = 0
        totalTax = 0
        total = 0
        for cartItem in self.__cartItemList:
            subtotal += cartItem.getProduct().getitemPrice() * cartItem.getQuantity()
            totalTax += subtotal * ShoppingCart.salesTax
            total += totalTax + subtotal

        print("Your Subtoal is:  $" + str(round(subtotal, 2)) + '\n'
              + "Your Tax is:  $" + str(round(totalTax, 2)) + '\n'
              + "Your total is:  $" + str(round(total, 2)) + '\n'
              + "Thank you for shopping with us! ")

def main():

    cart = ShoppingCart()

    pl = open('Products.csv', 'r')

    inventory = []

    for line in pl:
        lineList = line.split(',')
        p = Products(lineList[0], float(lineList[1]))
        inventory.append(p)

    print("Please selecet from the options below:")
    print("1: List of movies")
    print("2: Add Movie to Cart")
    print("3: Remove from Cart")
    print("4: Cart")
    print("5: Checkout")
    print("0: Leave store")

    try:
        menuNumber = int(input("What would you like to do?: "))
        print(" ")

        userChoice = menuNumber

        while userChoice !=0:

            if(userChoice == 1):
                try:
                    listAllProducts(inventory)

                except ValueError:
                    print(" Must be a valid number between 1-5")

            elif(userChoice == 2): # add to cart
                try:
                    listAllProducts(inventory)
                    cart.addCartItem(inventory)

                except ValueError:
                    print(" Must be a valid number between 1-5")

            elif(userChoice == 3): #remove from cart
                try:
                    cart.removeCartItem()
                except ValueError:
                    print("Please enter a valid number between 1-5")

            elif(userChoice == 4): #show cart
                print(cart)

            elif(userChoice == 5):  #checkout, and show total
                (cart.calculateTotal())

            else:
                print("Thank you for shopping with us")

            print(" ")

            userChoice = int(input("What would you like to do:  "))

    except ValueError:
        print('ERROR: Must be a valid number between 0 - 5')

def listAllProducts(inventory):
    seqNumber = 1
    for p in inventory:
        print(seqNumber, end='\t')
        p.display()
        seqNumber += 1

main()
