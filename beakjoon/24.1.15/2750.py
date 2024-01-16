# 첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000)이 주어진다. 둘째 줄부터 N개의 줄에는 수가 주어진다. 
# # 이 수는 절댓값이 1,000보다 작거나 같은 정수이다. 수는 중복되지 않는다.

l_len = int(input())
i_list = []

for i in range (l_len):
  i_list.append(int(input()))

i_list.sort(reverse=True)

for i in range(l_len):
  print(i_list.pop())

# while True:
#   try:
#     print(i_list.pop())
#   except:
#     False


## * Optimizing ##
# i=iter(open(0))
# next(i)
# print(*sorted(map(int,i)),sep='\n')

## * Other Answer ##
# import sys

# n = int(input())
# arr = [int(sys.stdin.readline()) for i in range(n)]
# arr.sort()
# print(*arr, sep="\n")
