# d - 병렬 개발에 걸리는 시간 / n - 프로그램 실행횟수 / s, p - 병직렬, 병렬 실행 시간


r = int(input())

for _ in range(r):
  d, n, s, p = map(int, input().split())
  if n * s < (d + (n * p)):
    print("do not parallelize")
  elif (n * s) == (d + (n * p)):
    print("does not matter")
  else:
    print("parallelize")
