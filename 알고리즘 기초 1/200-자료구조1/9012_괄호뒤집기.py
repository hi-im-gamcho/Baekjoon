for _ in range(int(input())):
    value = input()
    cnt = 0
    result = "1"


    for i in value:
        if i == "(":
            cnt += 1
        elif i == ")":
            cnt -= 1
        
        if cnt < 0:
            result = "NO"
            break
    
    if result == "NO":
        print(result)
    else:        
        if cnt == 0:
            print("YES")
        else:
            print("NO")