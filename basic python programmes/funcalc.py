# calculator using functions


def add(num1, num2):
    ans = num1 + num2
    return ans


def sub(num1, num2):
    ans = num1 - num2
    return ans


def mult(num1, num2):
    ans = num1 * num2
    return ans


def dev(num1, num2):
    ans = num1 / num2
    return ans


def pow(num1, num2):
    ans = num1 ** num2
    return ans


""" end of functions
 the so called main"""


rep = 'yes'
while rep == 'yes':
    num1 = float(input('Enter number 1 : '))
    print('Enter one of the following operator :\n+ - * / ^ ')
    op = input('Operator : ')
    num2 = float(input('Enter number 2 : '))
    if op == '+':
        ans = add(num1, num2)
    elif op == '-':
        ans = sub(num1, num2)
    elif op == '*':
        ans = mult(num1, num2)
    elif op == '/':
        ans = dev(num1, num2)
    elif op == '^':
        ans = pow(num1, num2)
    else:
        print('Invalid input .....Exiting ')
        exit()

    print(num1, op, num2, '=', ans)
    rep = input('Do you want to countinue(yes/no) ? :')
