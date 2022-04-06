N = int(input())                
result = N                      
                                

for i in range(N):
    word = input()              # apple
  
    for x in range(len(word)-1):    # 0 ~ 4
        if word[x] == word[x+1]:
            pass
        elif word[x] in word[x+1:]:
            result -= 1
            break

print(result)