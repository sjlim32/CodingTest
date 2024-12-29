# 테스트 케이스의 수 T(1<=T<=1,000)
# 0과 1로만 이루어진 이진수 숫자 2개, 길이는 최대 80자리 (덧셈 결과는 81자리가 될 수도 있다), 이진수는 0으로 시작할 수도 있다.

# 1 + 1 + 1 = 11
# 1 + 1 = 10

import sys
input = sys.stdin.readline
print = sys.stdout.write

def binary_addtion(a: str, b: str) -> str:
  num = int(a) + int(b)
  bi = list(str(num))
  stk = 0

  for j in range(len(bi) - 1, -1, -1):
    if int(bi[j]) + stk == 3:
      stk = 1
      bi[j] = 1
    elif int(bi[j]) + stk == 2:
      stk = 1
      bi[j] = 0
    elif int(bi[j]) + stk == 1:
      stk = 0
      bi[j] = 1

  if stk == 1:
    bi.insert(0, 1) 
  result = ''.join(map(str, bi))
  print(f"{result}\n")
    
if __name__ == '__main__':
  for i in range(int(input())):
    a, b = input().split()
    binary_addtion(a, b)

# OPTIMIZING

from sys import stdin
input = stdin.readline

for _ in range(int(input())):
    a, b = input().split()
    print(bin(int(a, 2) + int(b, 2))[2:])