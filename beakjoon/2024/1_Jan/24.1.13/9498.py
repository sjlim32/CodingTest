# 시험 점수를 입력받아 90 ~ 100점은 A, 80 ~ 89점은 B, 70 ~ 79점은 C, 60 ~ 69점은 D, 나머지 점수는 F를 출력하는 프로그램을 작성하시오.

grade = int(input())
if grade <= 100:
  print("A") if grade >= 90 else print("B") if grade >= 80 else print("C") if grade >= 70 else print("D") if grade >= 60 else print("F")
else:
  print("Out range")  