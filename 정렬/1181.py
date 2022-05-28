words = set() 

for i in range(int(input())):
    words.add(input())

words = list(words)
words.sort()            # 알파벳순으로 정렬     (a)
words.sort(key=len)     # 길이순으로 정렬       (b)

for word in words:
    print(word)


# 문제 조건

# 1. 길이가 짧은 것부터
# 2. 길이가 같으면 알파벳 순으로.

# 따라서 b -> a 로 해야함.