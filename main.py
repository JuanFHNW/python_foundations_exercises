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

#while loop example
name = ""
count = 0
while not name and count <5:
    count +=1
    name = input ("What is your name? ")
    if name:
        print(f"The is given: {name}")
    else:
        print("No name is given")


# for loop example
prices = [11.20, 35.40, 14.20]
total = 0

for price in prices:
    total += price

print(total)

