word = input().upper()              # 대문자로 통일 / Mississipi -> MISSISSIPI
word_set = list(set(word))          # (M, I, S, P) / 'set' object는 count 함수를 적용 할 수 없다. 
result = []

for i in word_set:
    result.append(word.count(i))    # result = [1, 4, 4, 1]
            
if result.count(max(result)) > 1:   # 최댓값의 개수가 1개 이상이라면
    print('?')
else :
    print(word_set[result.index(max(result))])
