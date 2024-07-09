from collections import deque

# deque 생성
dq = deque(['a', 'b', 'c'])

# 요소 추가
dq.append('d')
dq.appendleft('z')

# 요소 제거
dq.pop()
dq.popleft()

print(dq)  # deque(['b', 'c'])
