# to check if the given number is palindrome or not

print('Enter a number ')
num = int(input('NUMBER : '))
rev = 0
temp = num
while num > 0:
    b = num % 10
    rev = (rev * 10) + b
    num = num // 10

if temp == rev:
    print('Palindrome')
else:
    print('Not a Palindrome')
