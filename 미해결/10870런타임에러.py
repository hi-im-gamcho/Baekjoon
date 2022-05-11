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

# 이거 다이나믹 프로그래밍으로 했는데 왜 런타임에러 뜨는거지?
# 메모화 했는데...