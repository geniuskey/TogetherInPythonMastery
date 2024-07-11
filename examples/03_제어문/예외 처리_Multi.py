try:
    # 예외가 발생할 가능성이 있는 코드
    value = int(input("숫자를 입력하세요: "))
    result = 10 / value
except ValueError:
    # 숫자가 아닌 값을 입력한 경우
    print("유효한 숫자를 입력하세요.")
except ZeroDivisionError:
    # 0을 입력한 경우
    print("0으로 나눌 수 없습니다.")
