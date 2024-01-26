# 나무 판자는 크기 1의 너비를 가졌고, 양수의 길이를 가지고 있다. 
# 기훈이 방은 직사각형 모양이고, 방 안에는 벽과 평행한 모양의 정사각형으로 나누어져 있다.
# 이제 ‘-’와 ‘|’로 이루어진 바닥 장식 모양이 주어진다. 
# 만약 두 개의 ‘-’가 인접해 있고, 같은 행에 있다면, 두 개는 같은 나무 판자이고, 
# 두 개의 ‘|’가 인접해 있고, 같은 열에 있다면, 두 개는 같은 나무 판자이다.
# 기훈이의 방 바닥을 장식하는데 필요한 나무 판자의 개수를 출력하는 프로그램을 작성하시오.

# 첫째 줄에 방 바닥의 세로 크기 N 과 가로 크기 M 이 주어진다. 
# 둘째 줄부터 N개의 줄에 M개의 문자가 주어진다. 
# 이것은 바닥 장식 모양이고, '-‘와 ’|‘로만 이루어져 있다. 
# 
# N과 M은 50 이하인 자연수이다.

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

visited=set()

def DFS(y, x, tile):
  if y < columns and x < rows:
    if (y, x) not in visited:
      if arr[y][x] == '-' and arr[y][x] == tile:
        DFS(y, x+1, tile)
      elif arr[y][x] == '|' and arr[y][x] == tile:
        DFS(y+1, x, tile)
      else: return

      visited.add((y, x))

if __name__ == '__main__':
  columns, rows = map(int, input().split())
  arr = [list(input().strip()) for _ in range( columns )]
  result = 0

  for y in range(columns):
    for x in range(rows):
      if (y, x) not in visited:
        DFS(y, x, arr[y][x])
        result += 1


  print(result)