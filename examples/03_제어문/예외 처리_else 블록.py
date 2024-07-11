try:
    value = int(input("숫자를 입력하세요: "))
    result = 10 / value
except ValueError:
    print("유효한 숫자를 입력하세요.")
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")
else:
    print("결과는:", result)
