x = 50
y = 5
z = 6
answer = x - y*z
print(answer)

#floor division
print(17//3)

x = 10
z = "10"

print(x == z)

name = "John"
age = 10

message = "Hi, I'm " + name + ". My age is " + str(age)

#string operator
message2 = "Hi, I'm {}. My age is {}".format(name,str(age))

print(message)
print(message2)

myName = input("What is your name?: ")
age = input("How old are you?: ")
address = input("Where do you live?: ")

print(myName)
result = "Ah! Your name is {} and you live in {} and you're {} years old."

newName = "John Doe"

print(newName[0])

msg = "Hello! I'm John Doe. I'm from Japan and I love to play football.".split("Doe.")
print(msg)

test = ['a', 'b', 'c']
result = ''.join(test)
print(result)

letters = "aabbcc"
newLetters = letters.replace("b", "z")
print(newLetters)
hello = "      HelloWorld"
print(hello)
spaces = hello.strip()
print(spaces)
