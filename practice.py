print("hello world")
print("hello world")
print("hello world and iam learning it")
int
a = 2
int
b = 2
print(a + b)
apple = """hey, im a good girl 
and i want to go to school 
he has a bidg house """
print(apple)
print(apple[0], apple[1])
for character in apple:
    print(character)
fruit = "mango"
mangolen = len(fruit)
print(mangolen)
print(fruit[0:3])  # including 0 but not 3
print(fruit[0:-3])
nm = "#har ry###"
print(nm[-4:-2])

print(nm.upper())
print(nm.lower())
print(nm.rstrip("#"))
print(nm.replace("harry", "irma"))
print(nm.split(" "))
heading = "hello hru"
print(heading.capitalize())
str1 = "welcome "
print(str1.center(50))
print(nm.count("irma"))
str1 = "welcome to console!!"
print(str1.endswith("!!"))
str1 = "welcome to console!!"
print(str1.find("to"))
str1 = "0hello"
print(str1.isalnum())
print(str1.isalpha())
str1 = "hello world"
print(str1.islower())
str1 = "He's name is Dan. Dan is an honest man."
print(str1.title())
str1 = "Python is a Interpreted Language"
print(str1.swapcase())
age = int(input("What is your age: "))
print("Your age is: ", age)
if age > 18:
    print("you are allowed")
elif age == 18:
    print("allowed")
else:
    print("you are not allowed")
