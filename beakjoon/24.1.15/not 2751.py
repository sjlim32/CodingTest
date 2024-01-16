# 첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000,000)이 주어진다. 
# 둘째 줄부터 N개의 줄에는 수가 주어진다. 이 수는 절댓값이 1,000,000보다 작거나 같은 정수이다. 수는 중복되지 않는다.



# n = int(input())
# arr = [int(sys.stdin.readline()) for i in range(n)]
# arr.sort()
# print(*arr, sep="\n")

# ! 정렬 함수 직접 구현하기 

# NlogN 이하의 복잡도를 갖도록 해야함. ex) 병합 정렬 (merge), 힙 정렬 (heap), 기수 정렬, 카운팅 정렬
# 주어지는 원소 수는 최대 100만개, 즉 배열의 크기가 충분히 커야함
# 입력되는 정수의 값은 -1,000,000 에서 +1,000,000 까지
# Python은 매우 느립니다. 직접 정렬을 구현해서는 시간 보너스를 감안하더라도 통과하기가 매우 힘듭니다. PyPy2나 PyPy3로 제출해 보세요.
# 피벗을 랜덤으로 잡은 퀵소트를 구현하거나 힙소트, 머지소트 등 다른 O(nlogn) 정렬 알고리즘을 구현하는 방법이 있습니다.

import sys
input = sys.stdin.readline
print = sys.stdout.write

line = int(input())
n_list = list(map(int, [input() for _ in range(line)]))

def quick_sort(list, left, right):
  pl = left
  pr = right
  pivot = list[(left +right) // 2]

  while pl <= pr:
    while list[pl] < pivot: pl += 1
    while list[pr] > pivot: pr -= 1
    if pl <= pr:
      list[pl], list[pr] = list[pr], list[pl]
      pl += 1
      pr -= 1

  if left < pr: quick_sort(list, left, pr)
  if pl < right: quick_sort(list, pl, right)

quick_sort(n_list, 0, line-1)

for i in range (line):
  print(str(n_list[i])+"\n")