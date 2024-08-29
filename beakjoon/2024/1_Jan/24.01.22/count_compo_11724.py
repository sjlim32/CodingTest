# 방향 없는 그래프가 주어졌을 때, 연결 요소 (Connected Component)의 개수를 구하는 프로그램을 작성하시오.
# 첫째 줄에 정점의 개수 N과 간선의 개수 M이 주어진다. (1 ≤ N ≤ 1,000, 0 ≤ M ≤ N×(N-1)/2)
# 둘째 줄부터 M개의 줄에 간선의 양 끝점 u와 v가 주어진다. (1 ≤ u, v ≤ N, u ≠ v) 같은 간선은 한 번만 주어진다.
import sys
from collections import deque, defaultdict
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M = map(int, input().split())

g = defaultdict(list)
visited = set()
ans = 0

# 양방향 리스트 생성
for _ in range(M):
  s, e = map(int,input().split())
  g[s].append(e)
  g[e].append(s)

# def dfs(s):
#   visited.add(s)
  
#   for next_v in g[s]:
#     if next_v not in visited:
#       dfs(next_v)

# for v in range(1, N+1):
#   if v not in visited:
#     dfs(v)
#     ans += 1

# print(ans)

def bfs(s):
  q = deque([s])
  visited.add(s)

  while q:
    curr_n = q.popleft()

    for next_n in g[curr_n]:
      if next_n not in visited:
        visited.add(next_n)
        q.append(next_n)

for v in range (1, N+1):
  if v not in visited:
    bfs(v)
    ans += 1

sys.stdout.write(str(ans))