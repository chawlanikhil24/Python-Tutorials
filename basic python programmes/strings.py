# programme to calculate number of spaces in a string
str = input('Enter a string : ')
space = 0
vovels = 0
char = 0
for x in str:
    if x == ' ':
        space += 1
    elif x == 'a' or x == 'A' or x == 'e' or x == 'E' or x == 'i' or x == 'I' or x == 'o' or x == 'O' or x == 'u' or x == 'U':
        vovels += 1
    if x != ' ':
        char += 1

print("Number of spaces : ", space)
print("Number of vovels : ", vovels)
print("Number of characters : ", char)
