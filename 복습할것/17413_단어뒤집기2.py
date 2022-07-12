# (https://jeongm1n.tistory.com/entry/%EB%B0%B1%EC%A4%80-17413-%EB%8B%A8%EC%96%B4-%EB%92%A4%EC%A7%91%EA%B8%B0-2-Python)
# 아 뭔가 단순한것 같으면서도 잘 안되서 개고생했네...
# 알게 된 것 : 'ans'는 문자열 이라는 뜻
import sys

input = sys.stdin.readline

s = input().rstrip()
flag = False
word = ""
answer = ""

for i in s:
    if flag == False:
        if i == "<":
            flag = True
            word += i
        elif i == " ":
            word += i
            answer += word
            word = ""
        else:
            word = i + word

    else:
        word += i
        if i == ">":
            flag = False
            answer += word
            word = ""

print(answer + word)

        