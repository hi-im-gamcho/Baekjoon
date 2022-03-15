T = int(input())                    # 테스트케이스  2

for i in range(1, T+1):
    R, S = input().split()          # r=3 / s=abc
    result = ""                     #@@@@@@@@@@@@@@ 결과를 저장할 '문자열'@@@@@@@@@@@@ 이 생각을 못했음...
    for i in S:                     
        result += int(R) * i
    print(result)

# @@@@@@@@@@@@@@@for문을 이용하여 '문자열의 각 문자'에 접근할 수 있다@@@@@@@@@@@@@

