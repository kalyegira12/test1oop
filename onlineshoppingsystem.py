#introducing product class
class product:
    #initializing the details
    def __init__(self, productname, price, quality_in_stock):
        self.productname = productname
        self.price = price
        self.quality_in_stock = quality_in_stock

    #method to display the product
    def display_product_info(self):
        print(f"product: {self.productname}, price: {self.price}, stock: {self.quality_in_stock}")

#defining class shoppingcart
class shoppingcart:
    #class variable to track the number carts
    totalcarts = 0 

    #initializing cart details
    def __init__(self):
        self.items = []
        shoppingcart.totalcarts += 1 #a new cart has been added

    #how to add a product to the cart
    def addtocart(self, product, quatity):

    # how to remove a product
     def removeproduct(self, product):
         self.items = [(item, quatity) for item, quatity in self.items if item != product] 

    #how to calculate the total price of products in cart
    def calculatetotal(self):
        total = sum(product.price * quality for product, quality in self.items)
        return total
    
        # Method to display all items in the cart
    def display_cart(self):
        if not self.items:
            print("empty cart.")
        else:
            for product, quantity in self.items:
                print(f"{product.productname}: {quantity} @ {product.price} each")

# putting prices and quantities
pdt1 = product("kisuubitea", 3000, 5)
pdt2 = product("kazire", 1200, 4)
pdt3 = product("blanket", 200000, 2)

# the carts
cart1 = shoppingcart()
cart2 = shoppingcart()

#the operations on cart1
cart1.addtocart(pdt1, 3)
cart1.addtocart(pdt3, 5)
cart1.addtocart(pdt2, 8)
cart1.display_cart()
print(f"products in your cart1: shs{cart1.calculatetotal():.2f}\n")

# the operations in cart2
cart2.addtocart(pdt1,2)
cart2.addtocart(pdt3,7)
cart2.display_cart()
print(f"totalforcart2: shs{cart2.calculatetotal():.2f}\n")

#displaying all product information after transaction
print("stock after transaction:")
pdt1.display_product_info()
pdt2.display_product_info()
pdt3.display_product_info()