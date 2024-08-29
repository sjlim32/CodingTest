# 일부 학생들의 키를 비교한 결과가 주어졌을 때, 줄을 세우는 프로그램을 작성하시오.

# 첫째 줄에 학생들을 앞에서부터 줄을 세운 결과를 출력한다. 
# 답이 여러 가지인 경우에는 아무거나 출력한다.

# ? 위상정렬
# ? 사이클이 없는 "방향 그래프"의 모든 노드를 방향성에 거스르지 않도록, 순서대로 나열하는 것
# ? 모든 원소를 방문하기 전에 큐가 빈다면, 사이클이 존재하는 것 ( 보통 큐로 구현 )

import sys
from collections import deque
input = sys.stdin.readline
print = sys.stdout.write

# 진입차수가 0인 노드를 큐에 넣음
# 큐에 노드가 존재하면, 꺼내서 인접 노드 확인
# 확인한 인접 노드들을 방문한 적이 없어서 이번에 방문했다면, 진입차수 1 감소
# 만약 이번 방문으로 진입차수가 0이 된 노드가 있다면, 큐에 추가
def lining():
  result = []
  q = deque()

  for i in range(1, n + 1):
    if indegree[i] == 0:
      q.append(i)

  while q:
    curr_student = q.popleft()
    result.append(curr_student)

    for next_student in graph[curr_student]:
      indegree[next_student] -= 1

      if indegree[next_student] == 0:
        q.append(next_student)

  for res in result:
    print(str(res) + '\n')

if __name__ == "__main__":
  # 학생의 수, 비교한 횟수
  n, m = map(int, input().split())

  indegree = [0] * (n + 1)
  graph = [ [] for _ in range(n + 1) ]

  for _ in range(m):
    short, long = map(int, input().split())
    graph[short].append(long)
    indegree[long] += 1

  lining()
