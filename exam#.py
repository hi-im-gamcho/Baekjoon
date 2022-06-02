import sys

input = sys.stdin.readline

n = int(input().rstrip())
nums = list(map(int, input().split()))
result = {num: 1 for num in nums}


print(result)
    
