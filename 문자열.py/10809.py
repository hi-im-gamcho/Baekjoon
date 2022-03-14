word = input()
alphabets = list(range(97, 123))    # 알파벳의 아스키코드 범위

for alphabet in alphabets:
    print(word.find(chr(alphabet)))
