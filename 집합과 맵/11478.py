S = input()
S_list = []
                                    # a, b, c, d, e
for p in range(0, len(S)):          # 0, 1, 2, 3, 4
    for q in range(p, len(S)):           
        S_list.append(S[p:q+1])

print(len(set(S_list)))