n = int(input())

value = 2

while n != 1:
    if n % value == 0:
        print(value)
        n = n // value
    else:
        value += 1
    