# generate first n numbers of the fibonacci series

def fibonacci(n):

    if n == 1 or n == 0:
        return n;

    else:
        return fibonacci(n-2) + fibonacci(n - 1)
    

numero = int(input("enter your valid  number: "))

if numero<0:
    print("Number is not valid")

i = 0

print("Slect the fibonacci: ")


for i in range(0, numero):
    print(fibonacci(i))