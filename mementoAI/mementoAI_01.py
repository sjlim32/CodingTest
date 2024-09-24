# 문제 설명
# 함수 solution은 정수 x와 자연수 n을 입력 받아, x부터 시작해 x씩 증가하는 숫자를 n개 지니는 리스트를 리턴해야 합니다. 
# 다음 제한 조건을 보고, 조건을 만족하는 함수, solution을 완성해주세요.

def solution(x: int, n: int):
  if n < 1 or n > 1000 or x < -10000000 or x > 10000000:
    return
  
  answer = list(map(lambda i: x * i, range(1, n + 1)))
  return print(answer)

x = int(input())
n = int(input())
solution(x, n)