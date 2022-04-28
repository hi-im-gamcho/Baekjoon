list_a = ['요소1', '요소2', '요소3']

for i, value in enumerate(list_a):
    print(f'index : {i}, value : {value}') 

print(f"리스트에 enumerate 함수를 적용한 출력 형태 : {list(enumerate(list_a))}")