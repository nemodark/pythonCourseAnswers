speed = input("What is your current speed?")

if int(speed) <= 60:
    print("The top speed is 60kph!")
elif int(speed) <= 100 and int(speed) > 60:
    print("The top speed is 100kph!")
else:
    print("The top speed is until 100kph only")



number = input("Write a random number: ")

if(int(number)%2 == 0):
    print("The number is even.")
elif(int(number)%2 == 1):
    print("The number is odd.")

num = 3%2
print(num)