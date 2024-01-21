# 첫째 줄에 정점의 개수 V(1 ≤ V ≤ 10,000)와 간선의 개수 E(1 ≤ E ≤ 100,000)가 주어진다. 
# 다음 E개의 줄에는 각 간선에 대한 정보를 나타내는 세 정수 A, B, C가 주어진다. 
# 이는 A번 정점과 B번 정점이 가중치 C인 간선으로 연결되어 있다는 의미이다. 
# C는 음수일 수도 있으며, 절댓값이 1,000,000을 넘지 않는다.

# ? kruskal Algorithm
# ? 가중치의 오름차순으로 정렬해 놓은 뒤, 사이클을 형성하지 않는 선에서 정렬된 순서대로 간선을 선택
# Union-Find 란?
# Disjoint Set (서로소 집합) 을 표현하는 자료구조
# 서로 다른 두 집합을 병합하는 Union 연산, 집합 원소가 어떤 집합에 속해있는지 찾는 Find 연산을 지원하기에 이러한 이름이 붙었음

import sys
input = sys.stdin.readline

# vertexs[a]가 a가 아닌 경우(vertex 리스트는 value가 인덱스 번호 순으로 되어있음), vertex[a]에 할당되어 있는 값을 리턴
def find_node(vertexs, a):
  if vertexs[a] != a:
    vertexs[a] = find_node(vertexs, vertexs[a])
  return vertexs[a]

def union_parent(vertexs, a, b):
  a = find_node(vertexs, a)
  b = find_node(vertexs, b)
  
  if a < b:
    vertexs[b] = a
  else:
    vertexs[a] = b

node, edge = map(int, input().split())

edges = []
result = 0

# 1부터 node 까지 노드배열 생성
vertexs = [ i for i in range(node+1)]

for _ in range(edge):
# 시작 노드, 도착 노드, 노드 사이의 가중치를 저장
  start, end, weight = map(int, input().split())
  edges.append([start, end, weight])

# 가중치를 기준으로 오름차순 정렬
edges.sort(key=lambda edge: edge[2])

# find_node (p, a) 와 (p, b) 값이 서로 다르면, vertexs 리스트의 값을 작은 쪽으로 통일
# 통일하는 이유 = a가 b 보다 작을 때, 가중치가 오름차순으로 정렬되어 있기 때문에
# b번 노드로 가는 가장 빠른 길이 a 노드이기 때문에 다른 노드에서 방문하는 것을 배제하기 위함
for start, end, weight in edges:
  if find_node(vertexs, start) != find_node(vertexs, end):
    union_node(vertexs, start, end)
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