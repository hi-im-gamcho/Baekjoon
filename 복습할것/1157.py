word = input().upper()       # 대문자로 통일 / Mississipi
word_list = list(set(word)) # 중복되는 문자들을 없앰 / [M,I,S,P]
count_list = []

for i in word_list:
    cnt = word.count(i)     # cnt에 각 알파벳이 몇개 있는지 저장
    count_list.append(cnt)  # 리스트에 옮겨 담기 / [1,4,4,1]

# count_list의 최댓값의 개수가 1 이상이라면 '?' 를 출력
if count_list.count(max(count_list)) > 1:
    print('?')
else: 
    # 최댓값의 개수가 1개라면
    # max_index에 max의 인덱스 값을 저장함
    max_index = count_list.index(max(count_list))
    print(word_list[max_index])

# set()을 이용하면 문자열 내부의 중복을 없앨 수 있다!!! 

