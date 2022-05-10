import math

def prime_list(n):
    array = [True for x in range(n+1)]  # index 0 ~ n 까지 

    for i in range(2, int(math.sqrt(n)+1)): 
        if array[i] == True:                
            j = 2                          
            while i * j <= n:               
                array[i * j] = False
                j += 1
    
    prime_array = [i for i in range(2, n) if array[i] == True]
    
    a = n // 2
    b = n - a

    while a not in  prime_array and b not in  prime_array:
        a -= 1
        b += 1
    print(prime_array)
    print(a, b)

t = int(input())

for i in range(t):
    n = int(input())
    prime_list(n)

# 문제 : n 값에 20을 대입해보면 발생.

# [2, 3, 5, 7, 11, 13, 17, 19]
# 9 11  이렇게 나옴.

# while문에서 내가 의도했던건 a, b가 둘 다 prime_array에 들어있지 않는 한 계속 반복하라는 거 였는데
# 거기서 문제가 있는거같음. 
# 내가 의도한대로 할려면 어떻게 고쳐야하는지 궁금하고 내가 만든 while문이 의도와 어떻게 다른지 궁금쓰...