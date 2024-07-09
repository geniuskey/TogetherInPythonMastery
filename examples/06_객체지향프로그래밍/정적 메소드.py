class MathOperations:
    @staticmethod
    def add(a, b):
        return a + b


# 정적 메소드 호출
result = MathOperations.add(5, 3)
print(result)  # 8
