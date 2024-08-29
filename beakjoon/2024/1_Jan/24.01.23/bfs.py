from queue import Queue

GRAPH_SIZE = 1000  # 원하는 크기로 설정

def BFS(x, v):
    visited = [False] * GRAPH_SIZE
    q = Queue()
    q.put(x)  # 처음 방문할 노드를 큐에 담는다.
    visited[x] = True
    while not q.empty():  # 더 이상 다음에 방문할 노드가 없을 때까지
        next_node = q.get()  # 가장 먼저 방문한 노드를 소비하여, 해당 노드의 인접노드를 찾는다.
        print(next_node, end=' ')
        for value in v[next_node]:  # 해당 노드의 인접노드들을 반복하면서
            if visited[value]:  # 이미 방문한 노드라면 생략하고
                continue
            q.put(value)  # 그렇지 않다면 방문한다.
            visited[value] = True

# 예시 그래프
v = [[] for _ in range(GRAPH_SIZE)]
v[1] = [2, 3]
v[2] = [1, 4, 5]
v[3] = [1]
v[4] = [2]
v[5] = [2]

BFS(1, v)