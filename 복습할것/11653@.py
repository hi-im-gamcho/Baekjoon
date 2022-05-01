n = int(input())
i = 2

while n != 1:               
    if n % i == 0:          # 소인수분해 로직.
        n = n//i
        print(i)
    else: 
        i += 1 