# calculator
num1 = int(input('Enter first number : '))

print('Choose one of the following operators :')
print('1> +\n2> -\n3> *\n4> /\n5> ^ ')

op = input('Operator : ')

num2 = int(input('Enter second number : '))

ans = 1

if op == '+':
    ans = num1 + num2

elif op == '-':
    ans = num1 - num2

elif op == '*':
    ans = num1 * num2

elif op == '/':
    ans = num1 / num2

elif op == '^':
    ans = num1 ** num2

else:
    print('Invalid operator input..exiting')
    exit()

print(num1, op, num2, '=', ans)
