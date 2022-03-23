N = input()
count = 0   
N_list = list(map(int, N))
print(N_list)

for i in range(1, int(N)+1):              
    if i < 100:                    
        count += 1
    elif N_list[0] - N_list[1] == N_list[1] - N_list[2]:
        count += 1 
print(count)