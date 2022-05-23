import sys

y, x = map(int, sys.stdin.readline().split())

board = []
result = []
str1 = "WBWBWBWB"
str2 = "BWBWBWBW"
btw = [str2, str1, str2, str1, str2, str1, str2, str1]  # b부터 시작하는 체스판
wtb = [str1, str2, str1, str2, str1, str2, str1, str2]  # w부터 시작하는 체스판


for i in range(y):
    board.append(input())       # 입력받음

for a in range(0, y-7):         # y 좌표의 시작점 후보군
    for b in range(0, x-7):     # x 좌표의 시작점 후보군
        count = 0

        for p in range(8):      # 0 ~ 7
            for q in range(8):  # 0 ~ 7
                if board[a+p][b+q] != btw[p][q]:
                    count += 1
        result.append(count)
        count = 0

        for p in range(8):
            for q in range(8):
                if board[a+p][b+q] != wtb[p][q]:
                    count += 1
        result.append(count)
print(min(result))
                    

