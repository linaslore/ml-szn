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
