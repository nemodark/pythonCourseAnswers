
def calculate(time, items, price):

    subtotal = (float(price) * int(items))

    if int(time) >= 15:
        if int(items) >= 5:
            discount = subtotal * (20/100)
            totalPrice = subtotal - discount

        else:
            discount = subtotal * (10/100)
            totalPrice = subtotal - discount

    else:
        if int(items) >= 5:
            discount = subtotal * (10/100)
            totalPrice = subtotal - discount

        else:
            totalPrice = float(price)

    return totalPrice


name = input("Name: ")
time = input("Time: ")
items = input("Number of Items: ")
price = input("Price: ")

calc = calculate(time, items, price)

print("Total amount of {} is {}".format(name, calc))