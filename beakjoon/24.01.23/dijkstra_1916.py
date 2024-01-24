# 우리는 A번째 도시에서 B번째 도시까지 가는데 드는 버스 비용을 최소화 시키려고 한다. 
# A번째 도시에서 B번째 도시까지 가는데 드는 최소비용을 출력하여라. 

# N개의 도시가 있다. 
# 그리고 한 도시에서 출발하여 다른 도시에 도착하는 M개의 버스가 있다. 
# 도시의 번호는 1부터 N까지이다.
# start, end, weight

import sys, heapq

input = sys.stdin.readline
print = sys.stdout.write

INF = float('inf')
city = int(input()) 
bus = int(input())

distance = [INF]  * (city+1)
bus_route = { i:[] for i in range(1, city+1) }

# for _ in range(1, bus + 1):
#   bus_route.append(list(map(int, input().split())))

# bus_route.sort(key= lambda bus_route: bus_route[2])

for _ in range(1, bus + 1):
  start, end, cost = list(map(int, input().split()))
  # print("s, e, c", start, end, cost)
  bus_route[start].append((end, cost))

begin, arrive  = map(int, input().split())

# print("dist", distance)
# print("route", bus_route)
# print("b, a", begin, arrive)

def get_min_city(current):
  temp = INF
  min_city = 0

  for bus_info in bus_route[current]:
    if bus_info:
      print("bus", bus_info)
      arr_city, cost = bus_info

      if cost + distance[arr_city] < distance[arr_city]:
        distance[arr_city] = cost + distance[arr_city]

      if cost + distance[arr] > temp:
        continue
      else:
        min_city = bus_info
        temp = cost
        print('min_c', min_city)
        print('temp', temp)
    print("return", min_city)
    return min_city
  
  else:
    return -1

def dijkstra_bus(start, end):
  q = [(start, 0)]
  distance[start] = 0

  while q:
    current_city, cost = heapq.heappop(q)
    
    if distance[current_city] < cost:
      continue

    for next_city, price in bus_route[current_city]:
      next_c = cost + price
      
      if next_c < distance[next_city]:
        distance[next_city] = next_c
        heapq.heappush(q, (next_city, next_c))

dijkstra_bus(begin, arrive)
print(str(distance[arrive]))
    
# 출발 도시에서 큐에 넣음
# 출발 도시를 기준으로 거리값 초기화
# 출발 도시에서 인접 도시들에 대한 거리를 확인하면서 가장 짧은 거리인 도시 리턴
# 거리 가장 짧은 도시로 이동
# 거리가 가장 짧은 도시에서 기존 거리값과 새로 구한 거리값을 확인하여 둘 중 작은 값으로 거리값 초기화
# 마지막 도시까지 확인 후, 가야할 도시에 대한 거리값 리턴

