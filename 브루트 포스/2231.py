def hawai(n):
    for i in range(1, n+1):
        answer = []
        sum = i
        list_i = list(str(i))

        for x in list_i:
            sum += int(x)
        
        if sum == n:
            answer.append(sum)
            print(i)
            break

    if answer == []:
        print(0)

n = int(input())
hawai(n)


