number1 = 20
sign = '-'
number2 = 12

num1 = int(number1)
num2 = int(number2)

if sign == '+':
    print('Your result is ' + str(num1 + num2))

elif sign == '-':
    print('Your result is ' + str(num1 - num2))

elif sign == '*':
    print('Your result is ' + str(num1 * num2))

elif sign == '/':
    print('Your result is ' + str(num1 / num2))

else:
    print('Please enter +, -, * or /')



