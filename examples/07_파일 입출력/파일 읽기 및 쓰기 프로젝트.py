import csv

# 학생 성적 데이터
students = [
    {'name': 'Alice', 'math': 90, 'science': 85, 'english': 88},
    {'name': 'Bob', 'math': 78, 'science': 81, 'english': 92},
    {'name': 'Charlie', 'math': 95, 'science': 89, 'english': 85}
]

# CSV 파일에 학생 성적 데이터 쓰기
with open('students.csv', 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=['name', 'math', 'science', 'english'])
    writer.writeheader()
    for student in students:
        writer.writerow(student)

# CSV 파일에서 학생 성적 데이터 읽기
with open('students.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)
