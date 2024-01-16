
# N개의 정수 A[1], A[2], …, A[N]이 주어져 있을 때, 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.

# 첫째 줄에 자연수 N(1 ≤ N ≤ 100,000)이 주어진다. 다음 줄에는 N개의 정수 A[1], A[2], …, A[N]이 주어진다. 
# 다음 줄에는 M(1 ≤ M ≤ 100,000)이 주어진다. 다음 줄에는 M개의 수들이 주어지는데, 이 수들이 A안에 존재하는지 알아내면 된다.
# 
#  모든 정수의 범위는 -231 보다 크거나 같고 231보다 작다.

import sys
input = sys.stdin.readline
# print = sys.stdout.write      # 문자열만 출력 가능


N = int(input())
A = sorted(list(map(int, input().split())))
M = int(input())
find_n = list(map(int, input().split()))


def binery_search(arr, target, start, end):
  if start > end:
    return 0
    
  pivot = (start + end) // 2

  if arr[pivot] == target:
    return 1
  elif arr[pivot] > target:
    return binery_search(arr, target, start, pivot-1)
  else:
    return binery_search(arr, target, pivot+1, end)

for target in find_n:
  print(binery_search(A, target, 0, N -1 ))


  ## * Optimizing ##
# n,a,m = input(), set(input().split()), input()
# print("\n".join((["1" if x in a else "0" for x in input().split()])))