from collections import defaultdict

# 기본 값이 리스트인 defaultdict 생성
dd = defaultdict(list)

# 존재하지 않는 키에 접근
dd['a'].append(1)
dd['b'].append(2)

print(dd)  # defaultdict(<class 'list'>, {'a': [1], 'b': [2]})
