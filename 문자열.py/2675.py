T = int(input())                    # 테스트케이스  2

for i in range(1, T+1):
    R, S = input().split()          # r=3 / s=abc
    result = ""                     # 결과를 저장할 '문자열'
    for i in S:
        result += int(R) * i
    print(result)


