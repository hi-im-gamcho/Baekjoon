m = int(input())
n = int(input())
sosu = []

for i in range(m, n+1):      # m 이상, n 이하
    not_sosu = 0

    if i == 1:
        pass
    else:  
        for x in range(2, i):
            if i % x == 0:
                not_sosu += 1
        if not_sosu == 0:
            sosu.append(i)
    
if sosu == []:
    print("-1")
else:
    print(sum(sosu))
    print(min(sosu))



    

    