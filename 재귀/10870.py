n = int(input())

database = {
    1: 1,
    2: 1
}

def fibo(n):
    if n in database:
        return database[n]
    else: 
        output = fibo(n-1) + fibo(n-2)
        database[n] = output
        return output

print(fibo(n))

