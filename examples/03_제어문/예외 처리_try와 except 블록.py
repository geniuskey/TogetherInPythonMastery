try:
    # 예외가 발생할 가능성이 있는 코드
    result = 10 / 0
except ZeroDivisionError:
    # 예외가 발생했을 때 실행할 코드
    print("0으로 나눌 수 없습니다.")
