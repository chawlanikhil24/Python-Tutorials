# factorial programme

n = int (input("Enter a number to find its factorial : "))
fact = n
for x in range(n):
    if x!=0:
        fact = fact * x
print(fact)