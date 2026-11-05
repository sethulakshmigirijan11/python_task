class product:
    def __init__(self,product_name,product_id,price,quantity):
        self.product_name=product_name
        self.product_id=product_id
        self.price=price
        self.quantity=quantity
    def display_product(self):
        print("product_name:",self.product_name)
        print("product_id:",self.product_id)
        print("price:",self.price)
        print("quantity:",self.quantity)
    def calculate_total(self):
        print("tatal_stock_value:",self.price*self.quantity)  
    def update_price(self,newprice):
        self.price=newprice
        print("price updated successfully")
        print("newprice:",self.price)
    # def purchase(self.quantity):
    #     if quantity<=0:
        #  print("please enter a valid quantity")
product1=product("laptop","p101",50000,5)
product2=product("mobile","p102",20000,10)
product3=product("headphones","p103",1500,20)
product1.display_product()
product1.calculate_total()
product2.display_product()
product2.calculate_total()
product3.display_product()
product3.calculate_total()