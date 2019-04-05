
class Car:
    def __init__(self, price, brand, gas):
        self.price = price
        self.brand = brand
        self.gas = gas
        print("Created!!")
    
    def getValues(self):
        message = "{} has a gas capacity of {}L. The price is {}".format(self.brand,self.gas, self.price)
        return message

#create an instance of the class
bmw = Car(2000, "BMW", 500)
honda = Car(1500, "Honda", 400)
ferrari = Car(5000, "Ferrari", 700)
print(bmw.getValues())
print(honda.getValues())
print(ferrari.getValues())


