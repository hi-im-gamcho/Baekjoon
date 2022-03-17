N = int(input())                # 입력받은 단어의 갯수
count = 0                       # 그룹 단어 갯수
                                # i와 i 사이에 다른 문자가 없으면 그룹단어
for i in range(1, N+1): 
    word = input()              # aabbbccb
    if len(word) == 1:          # 이 경우 무조건 그룹단어
        count += 1
    elif len(word) == 2:
        count += 1
    elif len(word) >= 3:
        dict = {}               # word의 요소들을 중복없이 저장
        # dict 내에 리스트를 선언해서 거기에 요소들의 인덱스들을 저장
        # 인덱스들이 연속되는 숫자라면 count += 1
        for x in word:                              
            if x in dict:                           # 15~18행 : 딕셔너리에 리스트를 추가하는 과정
                dict[x].append(word.index(x))       # 이걸 못해서 못푼문제... 
            else:                                   # 근데 word = apple 일 때 
                dict[x] = [word.index(x)]           # {'a': [0], 'p': [1, 1], 'l': [3], 'e': [4]}
                                                    # p의 요소 값으로 1, 2 가 아니라 1,1 인거 보면 
                                                    # 이것도 문제가 있네...;;
           

    

