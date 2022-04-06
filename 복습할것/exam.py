N = int(input())                # 입력받은 단어의 갯수
count = 0                       # 그룹 단어 갯수
                                # i와 i 사이에 다른 문자가 없으면 그룹단어

for i in range(N):
    word = input()              # apple
    new_word_list = []
    error = 0

    if len(word) == 1:          # 이 경우 무조건 그룹단어
        count += 1
    elif len(word) == 2:        # 이 경우도 무조건 그룹단어
        count += 1
    else:                       # word 길이가 3 이상일 때
        for x in range(len(N-1)):   # 0 ~ N-1
            if word[x] != word[x+1]:    # 옆 글자와 다르면
                new_word_list.append(word[x+1])     # new_word_list = [p, l, e]
                    if new_word_list.count(word[x]) > 0:
                        error += 1
