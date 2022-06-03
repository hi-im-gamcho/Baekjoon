# 1. 딕셔너리를 이용한 방법--------------------------------
import sys
input = sys.stdin.readline

n1 = int(input().rstrip())
card_list1 = list(map(int, input().split()))
result1 = {card: 1 for card in card_list1}
m2 = int(input().rstrip())
num_list1 = list(map(int, input().split()))


for num in num_list1:
    if result1.get(num, 0):
        print(1, end=' ')
    else:                       # 여긴 없어도 괜찮을듯? 
        print(0, end=' ')
        
# 2. 이분탐색을 이용한 방법--------------------------------

n2 = int(input().rstrip())
card_list2 = list(map(int, input().split()))
card_list2.sort()   # 이분탐색 위해 오름차순 정렬
m2 = int(input().rstrip())
num_list2 = list(map(int, input().split()))

for num in num_list2:
    start = 0
    end = n2 - 1
    while True:
        mid = (start + end) // 2 
        if card_list2[mid] == num:
            print(1, end=' ')
            break
        if card_list2[mid] < num:
            start = mid + 1
        if card_list2[mid] > num: 
            end = mid - 1
        if start > end:
            print(0, end=' ')
            break

# 3. 메모라이제이션 (Memorization) 이건 이 문제에 적용하기엔 상대적으로 비효율적인 거 같긴 하다-------------------------------

card = [0] * 20000001
N = int(input())
card1 = list(map(int, input().split()))
for i in card1:
    card[i + 10000001] = 1

M = int(input())
card2 = list(map(int, input().split()))
for i in card2:
    if card[i + 10000001]:
        print(1, end=' ')
    else:
        print(0, end=' ')