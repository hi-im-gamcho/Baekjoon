import math

def prime_list(n):
    array = [True for x in range(n+1)]  # index 0 ~ n 까지 

    for i in range(2, int(math.sqrt(n)+1)): # 여기가 이해 안감. 왜 n 의 최대 약수가 sqrt(n) 이하라는거지 
        if array[i] == True:
            j = 2
            while i * j <= n:
                array[i * j] = False
                j += 1
    
    print(array)
    return [i for i in range(2, n) if array[i] == True]
print(prime_list(23))

# 리스트 : [0, 1, 2, 3, 4, 5]
# 인덱스 : [0, 1, 2, 3, 4, 5]