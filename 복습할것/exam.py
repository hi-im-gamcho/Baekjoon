N = int(input())
num_group_word = N

for i in range(N):
    word = input()                      # apple

    for x in range(len(word)-1):
        if word[x] == word[x+1]:
            pass
        elif word[x] == word[x+1:]:
            num_group_word -= 1 
            break