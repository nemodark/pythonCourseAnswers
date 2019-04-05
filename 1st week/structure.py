
#List
height = [170, 172, 180, 175]

print(height[0])
height[0] = 200
print(height[0])
#append
height.append(250)
print(height)
# Insert before the index number
height.insert(1, 165)
print(height)

#delete a index value
height.pop(1)
print(height)

#remove will delete the value
height.remove(180)
print(height)

#delete all the values
# height.clear()
# print(height)

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(x[1:3])

#count the numbers inside a list
count = len(x)
print(count)

hello = "Hello World"
e = hello[1:5]
print(e)

#tuple 
z = (1, 2, 3, 4, 5)
newtuple = z + (6, 7)
print(newtuple)

#dictionary
cars = {"car1":"BMW", "car2":"Honda", "car3":"Ford"}
print(cars["car1"])

kredo_school = []
classA = ["Mike", "John", "Alex"]
classB = ["Clint", "Zob", "Amanda"]
classC = ["Tomy", "Bob", "Vijay"]

kredo_school.append(classA)
kredo_school.append(classB)
kredo_school.append(classC)
print(kredo_school)

#modulus
weight = 60
height = 1.7
#weight/height(m)2
answer = weight/height**2
print(answer)

grade = []

john = [80, 90, 75]
tom = [90, 85, 100]
bob = [85, 93, 81]

grade.append(john)
grade.append(tom)
grade.append(bob)
print(grade[0][0])