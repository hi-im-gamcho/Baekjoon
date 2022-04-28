n = int(input())

numbers = map(int, input().split())
sosu = 0


for number in numbers:
    error = 0
    if number == 1:     # 1은 소수가 아님.   
        pass
    else:               # 2이상의 자연수에 대해서
        for i in range(2, number):  # 2 ~ number-1
            if number % i == 0:
                error += 1
                break       # 이건 필요 없는거같아...
        if error == 0:
            sosu += 1

print(sosu)     