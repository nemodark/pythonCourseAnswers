
def helloWorld():
    print("Hello World")

helloWorld()

def add(x, z, y=10):
    total = x + z + y
    return total

num1 = add(10, 20, 20)
num2 = add(5, 10)
num3 = add(3, 9)

print(num1 + num2 + num3)

def hello():
    return "Hello"

def world():
    a = hello()
    return a + "World"

print(world())


def addList(myList):
    x = 0
    for i in myList:
        x += i
    return x

num = [1, 2, 3, 4, 5]

total = addList(num)

newList = [10, 20, 30]
newTotal = addList(newList)

print(total)
