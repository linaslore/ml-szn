#cel to far

cel_value = int(input("please enter the celcius value you want to convert: "))
far_value = (cel_value * 1.9)
print(f'the celcius value {cel_value} in farenheit is {far_value}')


#bmi, height and weigth needed
height = int(input("please enter your height: "))
weight = int(input("please enter your weight: "))

bmi = (weight/(height**2))
print(f'your bmi is {bmi}')


#split names

full_name= input("please enter your full name: ")
names = full_name.split( )
first_name = names[0]
last_name = names[1]

print(f'your first name is {first_name} and your last name is {last_name}')

#voting elgibility
age = int(input("please enter your age: "))
is_eligible = age >= 18
print(f'Eligible: {is_eligible}') 


#simple calculator
x = int(input("please input the first number: "))
y = int(input("please input the second number: "))

add = x + y
subtract = x - y
multiply = x * y
division = x / y
print(f"the addition of {x} and {y} is {add} and the subtraction: {subtract} and the multiplication {multiply}, and the divison is {division}")

#guessing game

secret_word = "alice"


while True:
    guess = input("please enter guess: ")
    if secret_word == guess:
        break
    print("you have guess incorrectly. try again")


print("done")


#multiplication table
for i in range(1, 11):
    for j in range(1, 11):
        print(i * j, end="\t")
    print()

# or
number = int(input("Enter a number: "))

for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")






## prime checker

x = int(input("please enter the number you want to check: "))
if x <=1:
    print(f"{x} is a prime number")
else:
    is_prime = True
    for i in range(2, x):
        if x % i == 0:
            is_prime = False
            break
    if is_prime:
        print(f'{x} is a prime number')
    else:
        print(f'{x} is not a prime number')



# #password validator
password = input("please enter a password that is at least 4 characters long and contains a number")

if len(password) >= 4:
    if any(char.isdigit() for char in password):
        print("valid ")
    else:
        print("please include a number in your password")
else:
    print("invalid")
