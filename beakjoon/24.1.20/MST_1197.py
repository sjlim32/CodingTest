# 첫째 줄에 정점의 개수 V(1 ≤ V ≤ 10,000)와 간선의 개수 E(1 ≤ E ≤ 100,000)가 주어진다. 
# 다음 E개의 줄에는 각 간선에 대한 정보를 나타내는 세 정수 A, B, C가 주어진다. 
# 이는 A번 정점과 B번 정점이 가중치 C인 간선으로 연결되어 있다는 의미이다. 
# C는 음수일 수도 있으며, 절댓값이 1,000,000을 넘지 않는다.


import sys
input = sys.stdin.readline

def find_parent(parent, a):
  if parent[a] != a:
    parent[a] = find_parent(parent, parent[a])
  return parent[a]

def union_parent(parent, a, b):
  a = find_parent(parent, a)
  b = find_parent(parent, b)
  
  if a < b:
    parent[b] = a
  else:
    parent[a] = b

node, edge = map(int, input().split())

edges = []
result = 0

parent = [ i for i in range(node+1)]
print(parent)

for _ in range(edge):
  start, end, weight = map(int, input().split())
  edges.append([start, end, weight])

edges.sort(key=lambda edge: edge[2])

for start, end, weight in edges:
  if find_parent(parent, start) != find_parent(parent, end):
    union_parent(parent, start, end)
    result += weight

sys.stdout.write(str(result))


## ! Wrong Answer..
# import sys
# input = sys.stdin.readline

# node, edge = map(int, input().split())
# edgeList = []
# result = 0
# selected = set()

# for _ in range(edge):
#   start, end, weight = map(int, input().split())
#   edgeList.append([start, end, weight])

# edgeList.sort(key=lambda edge: edge[2])

# n개의 정점을 가지는 그래프의 최소 간선의 수는 n-1개
# while len(selected) != node-1:
#   for i in range(edge):
# # 뒤의 간선 중에 이미 selected 된 node로 향하는 경우는 패스
#     if edgeList[i][1] in selected:
#       continue

# # 가중치가 가장 낮은 간선의 도착 node를 selected에 저장, 가중치는 msp에 저장
#     result += edgeList[i][2]
#     selected.add(edgeList[i][1])

# sys.stdout.write(str(result))