'''this programme converts asccii code to character
and a character into an ascii code'''
print("Choose an option from below : ")
print("1.covert ascii to character.")
print('2.Covert character to ascii')
i = int(input('Enter choice : '))
if i == 1:
    print('Enter a number from 1 - 256 ')
    num = int(input("NUMBER : "))
    print("your character : ", chr(num))
# chr returns a string of one character
elif i == 2:
    print('Enter a character ')
    char = input("CHARACTER : ")
    print("your number : ", ord(char))
# ord returns code for one character
else:
    print('Invalid input ')
