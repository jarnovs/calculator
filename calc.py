from os import system, name


# Function for clearing the console
def clear():
    system('cls' if name=='nt' else 'clear')
clear()

# Function for multiplication
def multiplication(a, b):
	res = a * b
	return res

# Function for division
def division(a, b):
	if b != 0: 
		res = a / b
		return res
	else:
		return 'Division by 0 is undefined'

# Function for subtraction
def subtraction(a, b):
	res = a - b
	return res

# Function for addition
def addition(a, b):
	res = a + b
	return res


a = float(input('Write the first number: '))
b = float(input('Write the second number: '))

operation = int(input('''
Choose the operation:
1- Multiplication
2- Division
3- Subtraction
4- Addition
'''))

clear()


# Results
if operation == 1:
	print(f'{a} * {b} = {multiplication(a, b)}')
elif operation == 2:
	print(f'{a} / {b} = {division(a, b)}')
elif operation == 3:
	print(f'{a} - {b} = {subtraction(a, b)}')
elif operation == 4:
	print(f'{a} + {b} = {addition(a, b)}')
else:
	print('Choose the operation between 1 and 4')
