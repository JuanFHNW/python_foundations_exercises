helloWorld = "Hello World"
print(helloWorld)
helloWorld = "Hello World 2"
print(helloWorld)

# python is caps sensitive
a = 1
b = 5

B = a / b
print(B)

# basic if statement
isPythonFun = True

if isPythonFun:
    print("Python is fun!" + "lol"*3)
else:
    print("Python is not fun :(")

name = input("What is your name? ")
print("Hello " + name)

# input is always a string, so we need to convert it to an integer
a = input("Enter the first number: ")
b = input("Enter the second number: ") 

result = int(a) + int(b)

print(result)
