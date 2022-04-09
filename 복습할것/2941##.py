alphabet = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

word = input() # ljes=njak

for i in alphabet:
    word = word.replace(i, '+')
print(len(word))

# replace 함수의 존재와 사용법을 알게됨.
# replace 함수와 for 을 조합하면 
# 문자열 내 모든 문자들을 치환할 수 있다는 것을 알게됨