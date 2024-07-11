age = int(input("나이를 입력하세요: "))

if age < 18:
    print("미성년자입니다.")
elif 18 <= age < 65:
    print("성인입니다.")
else:
    print("노인입니다.")
