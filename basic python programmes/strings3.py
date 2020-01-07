# programme to convert lower case letters in string to upper case
import string
text = input('Enter a string : ')
for x in text:
    if x in string.ascii_lowercase:
        text = text.replace(x, x.upper())

print('New string : ', text)
