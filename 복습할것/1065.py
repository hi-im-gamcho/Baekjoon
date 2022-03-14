N = int(input())

def hansu(N):
    count = 0
    for i in range(1, N+1):
        num_list = list(map(int, str(i)))
        # 100 보다 작으면 한수
        if i < 100:
            count += 1
        elif num_list[0] - num_list[1] == num_list[1] - num_list[2]:
            count += 1
    return count

print(hansu(N))  


