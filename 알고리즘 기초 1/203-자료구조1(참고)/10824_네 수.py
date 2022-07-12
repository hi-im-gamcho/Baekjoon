A,B,C,D = map(int, input().split())

AB = int(str(A)+str(B))
CD = int(str(C)+str(D))

print(AB + CD)

### 다른 풀이

nums = input().split()
print(int(nums[0]+nums[1])+int(nums[2]+nums[3]))
