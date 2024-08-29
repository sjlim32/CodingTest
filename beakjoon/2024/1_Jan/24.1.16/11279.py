# 널리 잘 알려진 자료구조 중 최대 힙이 있다. 
# 최대 힙을 이용하여 다음과 같은 연산을 지원하는 프로그램을 작성하시오.

# 배열에 자연수 x를 넣는다.
# 배열에서 가장 큰 값을 출력하고, 그 값을 배열에서 제거한다.
# 프로그램은 처음에 비어있는 배열에서 시작하게 된다.

from heapq import heappop, heappush
import sys

input = sys.stdin.readline
# print = sys.stdout.write

num_list = [int(input()) for _ in range(int(input()))]
h_list = []

for num in num_list:
  if num == 0 and len(h_list) == 0:
    print(0)

  elif num > 0:
    heappush(h_list, -num)
  
  elif num == 0:
    print(-heappop(h_list))

## * Optimizing ##
# [
#   heappush(h_list, -num) if num
#   else print(-heappop(h_list) if heap else 0)
#   for num in num_list
# ]



##### ! 시간 초과 (T.T )
# import sys
# input = sys.stdin.readline
# print = sys.stdout.write

# num_list = [int(input()) for _ in range(int(input()))]
# answer = []

# for idx, n in enumerate(num_list):
#   if n == False and len(answer) == 0:
#     print("\n0")
#   elif n == False and max(answer) == 0:
#     print("\n0")

#   elif n == False:  
#     m_num = max(answer)
#     print(f"\n{str(m_num)}")
#     answer.remove(m_num)

#   else:
#     answer.append(n)