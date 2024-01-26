# 세 개의 장대가 있고 첫 번째 장대에는 반경이 서로 다른 n개의 원판이 쌓여 있다. 
# 각 원판은 반경이 큰 순서대로 쌓여있다. 이제 수도승들이 다음 규칙에 따라 첫 번째 장대에서 세 번째 장대로 옮기려 한다.

# 한 번에 한 개의 원판만을 다른 탑으로 옮길 수 있다.
# 쌓아 놓은 원판은 항상 위의 것이 아래의 것보다 작아야 한다.
# 이 작업을 수행하는데 필요한 이동 순서를 출력하는 프로그램을 작성하라. 단, 이동 횟수는 최소가 되어야 한다.

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

def move_cnt(n):
  print(2**n -1)

def mover(n, fst, snd, trd):
  print(fst, trd)
  print(fst, snd)
  print(trd, snd)

def hanoi(n, start, so, end):
  if n ==1 :
    return None
  if n == 2:
    mover(n, start, end, so)

  if n == 3:
    mover(n-1, start, so, end)
    print(start, end)
    mover(n-1, so, end, start)

  elif n > 3:
    hanoi(n-2, start, so, end)
    print(start, so)
    hanoi(n-2, end, start, so)
    print(start, end)
    hanoi(n-1, so, start, end)
    
    return None

n = int(input())

if n == 1:
  print(1)
  print(1, 3)

elif n <= 20:
  move_cnt(n)
  hanoi(n, 1, 2, 3)

else:
  move_cnt(n)

# N 타워는 1 + 2 + ... + n -1 까지의 타워의 합
# 대신, 시작점이 다름. 
# n = 2 일때, 시작-끝은 1, 2

# n = 3 일때, 시작점 1, 끝점 3
# >>> (n-1)의 시작-끝은 1, 3
# >>> 1, 3 출력
# >>> (n-1)의 시작-끝 2, 1

# n = 4 일때, 시작점 1, 끝점 2
# >>> (n-1)의 시작-끝은 1, 2
# >>> 1, 3 출력
# >>> (n-1)의 시작-끝은 2, 3

## * Optimizing ##
