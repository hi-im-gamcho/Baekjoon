# 1. item()
# - '딕셔너리의' 키와 값을 조합해야할 때 사용.




# 2. 딕셔너리 내포
# -ex)
# card_list = list(map(int, input().split()))
# result = {card: 1 for card in card_list}      ->      만약 중복되는 card 가 있다면 중복을 없앤 채로 result를 만듦.
#  

# 해석
# card_list의 요소를 키 값으로 받아오고 거기에 대해 1을 할당함.




# 3. 딕셔너리에서 데이터 가져오기
# -1) dictionary[key]
#   - 해당하는 키 값이 없을 때는 에러가 발생한다.

# -2) dictionary.get(key, default)
#   - 해당하는 key 값이 없으면 none을 반환한다.
#   - 단, default를 설정했다면 default를 반환한다.



# 4. 딕셔너리에 데이터 집어넣기
S = {}
cnt = 0

for i in range(n):
    S[input()] = True

# 4-1 키가 있는 상태에서 값 추가하기
closet = {}

if key not in closet:
    closet[key] = [cloth]   # 키와 값 dict에 추가.
else:
    # 1. closet[key].append(cloth)
    # 2. closet[key] += ['cloth'] 로도 된다.

# 입력값
# hat headgear
# sunglasses eyewear
# turban headgear
# {'headgear': ['hat', 'turban'], 'eyewear': ['sunglasses']}



# 5. 딕셔너리의 문자열 키와 관련된 실수
# 딕셔너리의 키에 단순한 식별자를 입력하면, 이를 변수로 인식한다.
# 이를 해결하고 싶다면 식별자를 변수로 만들어주면 된다. 
# 따라서 키를 문자열로 사용할 때는 반드시 따음표("")를 붙여주자!!
# 해설

cloth, kind = map(str, input().split())
if kind not in closet:      # 여기에서 kind는 '변수'
    closet[kind] = [cloth]  # 여기에서 kind도 '변수'
                                # 만약 closet['kind']라고 해버리면 kind가 key에 해당하는 변수가 아니라
                                # 특정 key가 되어버리는거임!!!


# 6. 딕셔너리의 요소 제거
# def dictionary[키]



# 7. 딕셔너리 내부에 키가 있는지 확인하기 (in 키워드)
# if key in dictonary:
# for key in dictionary