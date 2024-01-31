print('if elif else - Exercise')
# Create a calculator which handles +,-,*,/ and outputs answer based on the mode/ operator used
# Hint: use 3 separate inputs 
# Bonus: Extend functionality with extra mode so it also does celsius to fahrenheit conversion
# formula is: temp in C*9/5 + 32 = temp in f
num1 = input('Input your first number:')
operand = input('Input the operation that you would like to perform').lower
num2 = input('Input the number that would be operated against')

if operand == '*' or operand == 'multiplication':
    result = float(num1) * float(num2)
    print(f'{num1} * {num2} = {result}')
elif operand == '/' or operand == 'division':
    result = float(num1) / float(num2)
    print(f'{num1} / {num2} = {result}')
elif operand == '+' or operand == 'addition':
    result = float(num1) + float(num2)
    print(f'{num1} + {num2} = {result}')
elif operand == '-' or 'subtraction':
    result = float(num1) - float(num2)
    print(f'{num1} - {num2} = {result}')

temperature_in_celsius = input('Input the temperature in Celsius')
temperature_in_fahrenheit = float(temperature_in_celsius) * 9 / 5 + 32
print(f'The temperature in Fahrenheit is {temperature_in_fahrenheit}')
