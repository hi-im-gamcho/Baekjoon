N = int(input())
# [] 에다가 입력받은 숫자를 sub_num에 넣음
subject= list(map(int, input().split()))
M = max(subject)
new_subj = []

# new_subj에 새로운 과목점수를 넣음
for i in subject:
    new_subj.append(i/M*100)

sum_all = sum(new_subj)
print(sum_all/N)