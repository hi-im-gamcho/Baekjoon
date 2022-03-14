C = int(input()) # C : 테스트케이스

for i in range(C):                                      # N = '학생의 수' / 각 테스트케이스마다 N이 다름
    N_and_scores = list(map(int, input().split()))      # 학생들의 점수를 리스트화
    sum_scores = sum(N_and_scores[1:])                  # 학생들의 점수의 총합
    avr = sum_scores / N_and_scores[0]                  # 학생들의 점수의 평균
    count = 0                               
    for score in N_and_scores[1:]:                        
        if score > avr:                         # 각 학생들의 점수하고 평균 비교해서
            count += 1                          # 평균넘으면 count += 1
    result = (count / N_and_scores[0]) * 100       
    print(f'{result:.3f}%')
    
                                         
