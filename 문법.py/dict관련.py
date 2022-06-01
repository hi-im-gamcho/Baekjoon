# 1. item()
# - '딕셔너리의' 키와 값을 조합해야할 때 사용.




# 2. 딕셔너리 내포
# -ex)
# card_list = list(map(int, input().split()))
# result = {card: 1 for card in card_list} 

# 해석
# card를 매개변수로 받아옴.
# card_list의 요소를 키 값으로 받아오고 거기에 대해 1을 할당함.




# 2. 딕셔너리에서 데이터 가져오기
# -1) dictionary[key]
#   - 해당하는 키 값이 없을 때는 에러가 발생한다.

# -2) dictionary.get(key, default)
#   - 해당하는 key 값이 없으면 none을 반환한다.
#   - 단, default를 설정했다면 default를 반환한다.