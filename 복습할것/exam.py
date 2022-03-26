n = int(input())        # 13

# 1
# 6 * 1
# 6 * 2
# 6 * 3

house = 1
cnt = 1

while n > house:        # 13 > 1    13>7        13<19
    house += 6*cnt      # 1+6=7     7+12=19
    cnt += 1            # cnt==2    cnt==3
print(cnt)
