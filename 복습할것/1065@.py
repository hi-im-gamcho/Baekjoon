N = int(input())

def hansu(N):
    count = 0
    for i in range(1, N+1):
        # N을 int형으로 바꾸고
        # 오마분시해서 리스트화
        num_list = list(map(int, str(i)))  
        # 100 보다 작으면 한수
        if i < 100:
            count += 1
        elif num_list[0] - num_list[1] == num_list[1] - num_list[2]:
            count += 1
    return count

print(hansu(N))  

# 내가 못했던 부분 : N이 등차수열인지 확인을 못함.
# 1. str(i)                     문자열화
# 2. list(str(i))               문자열을 오마분시
# 3. list(map(int, str(i)))     옆자리끼리 비교해야하니까 int형으로 바꿔줘야함


