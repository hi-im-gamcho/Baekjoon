result = []
word = input()

for i in range(len(word)):
    result.append(word[i:])
    
result.sort()
for i in result:
    print(i)
