class CustomError(Exception):
    pass


try:
    raise CustomError("이것은 사용자 정의 예외입니다.")
except CustomError as e:
    print(e)
