from collections import ChainMap

# 두 개의 딕셔너리 생성
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}

# ChainMap 생성
chain = ChainMap(dict1, dict2)

print(chain)  # ChainMap({'a': 1, 'b': 2}, {'c': 3, 'd': 4})
print(chain['a'])  # 1
print(chain['c'])  # 3
