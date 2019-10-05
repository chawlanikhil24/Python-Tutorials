# using lists as array
n = int(input('Enter the number of elements of the array : '))
arr = []
print('Enter the elements')
count = 0
for x in range(n):
    print('Element', count + 1, ':')
    ele = int(input())
    count += 1
    arr.append(ele)

print('Array = ', arr)
