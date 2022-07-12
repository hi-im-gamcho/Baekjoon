from sys import stdin
input = stdin.readline

n = int(input().rstrip())
sentence = input().rstrip()
stack = []
# 대문자에 대응하는 숫자를 담는 리스트 
nums = [int(input().rstrip()) for _ in range(n)]
for s in sentence:
    # 'A' ~ 'Z' 사이의 대문자라면
    if ord('A') <= ord(s) <= ord('Z'):
        # 대문자에 대응하는 숫자 저장
        number = nums[ord(s) - ord('A')]
        stack.append(number)
        continue
    # 대문자가 아닌 연산자라면
    w2 = stack.pop()
    w1 = stack.pop()
    result = eval(str(w1) + s + str(w2))
    stack.append(result)

print("%.2f"%stack[0])

### (https://dogsavestheworld.tistory.com/148)
### (https://animoto1.tistory.com/entry/%EB%B0%B1%EC%A4%80-1935-%ED%9B%84%EC%9C%84-%ED%91%9C%EA%B8%B0%EC%8B%9D2-%ED%8C%8C%EC%9D%B4%EC%8D%AC-Python)