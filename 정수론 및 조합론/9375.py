import sys

input = sys.stdin.readline

for _ in range(int(input())):   # T
    n = int(input())
    closet = {}

    for i in range(n):
        cloth, kind = map(str, input().split())
        if kind not in closet:
            closet[kind] = [cloth]
        else:
            closet[kind].append(cloth)  # 이미 key 가 있는 딕셔너리의 키에 값 추가하는 법.

    result = 1
    for key in closet:                  # 딕셔너리의 내부의 모든 key에 대해
        result *= (len(closet[key])+1)
    
    print(result - 1)
    


