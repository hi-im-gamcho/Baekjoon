from collections import Counter

num_list = [4000]

cnt = Counter(num_list).most_common()
print(cnt)
print(cnt[0][0])