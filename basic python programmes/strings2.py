# programme to remove all vovels from a string

vovels = ('a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U')
text = input('Enter a string : ')
for x in text:
    if x in vovels:
        text = text.replace(x, '')

print('New text : ', text)
