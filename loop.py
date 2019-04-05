
x = 5
for i in range(x):
    for z in range(i):
        print("*", end="")
    print('')

for i in range(x,0, -1):
    for j in range(i):
        print("*", end="")
    print('')

for i in range(5, 0, -1):
    print(i)

#Loops using a list

students = ["John", "Jane", "Joe"]

for student in students:
    print(student)

#while loop
x = 0
while x < 5:
    print(x)
    x += 1

#break
names = ['Alice', 'Bob', 'Charlie']

for name in names:
    if name == 'Bob':
        print('Exit')
        break
    print(name)

#continue
val = 0

while val < 10:
    if val == 4:
        print("skip!!")
        val+=1
        continue
    print(val)
    val += 1

i = 1
num = 0

while i < 56:
    num = i + num
    i += 1
    print(num, end=", ")

a = 0
b = 1
for i in range(0, 55):
    temp = a
    a = b
    b = temp + b
    print(a)
