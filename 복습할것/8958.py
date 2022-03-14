test_case = int(input())

for i in range(test_case):  # test_case만큼 반복
    qz_result = input()     # 문제의 결과를 입력받음. ex) OOXXOOXXOOXX
    final_score = 0         # 문제의 최종 점수
    score = 1               # 정답 시 배점 초기값
    for x in range(len(qz_result)):     # 입력받은 문자열의 길이(=문제 결과)를 이용
        if qz_result[x] == 'O':         # 각 문제의 결과가 O인지 X인지에 따라
            final_score += score # 최종 점수에 배점 등록
            score += 1           # 배점 올리기
        else:                    # 오답일 경우
            score = 1            # 배점을 초기값으로 초기화 (배점 초기화)
    print(final_score)

