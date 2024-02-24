# import sys
# input = sys.stdin.readline
# print = sys.stdout.write
# sys.setrecursionlimit(10**6)

def bin_search(arr: list[int], chk_list: list[bool], target: int) -> int:
  left, right = 0, len(arr) - 1

  while left <= right:
    pivot = (left + right) // 2
    
    if arr[pivot] == target:
        return pivot

    elif arr[pivot] < target:
      left = pivot + 1
    
    else:
      right = pivot -1
  
  return -1

def find_disCnt_price(result: int, price_list: list[int]) -> None:
  # res = []

  # for i in range(len(price_list) - 1, -1, -1):
  #   if price_list[i] % 4 == 0:
  #     chk_price = price_list[i] * 3 // 4

  #     if bin_search(price_list[:i], chk_price):
  #       res.append(chk_price)

  #   if len(res) == result:
  #     return res

  # return res

  # # ! 불리언 리스트 생성 후, 불리언 값 갱신
  chk_list = [False] * len(price_list)
  res = []
  cnt = 0
  chk_res = 0

  # O(n)
  for i in range(len(price_list) - 1, -1, -1):   
    if not chk_list[i] and price_list[i] % 4 == 0:
      chk_price = price_list[i] * 3 // 4
      chk_idx = bin_search(price_list[:i], chk_list, chk_price)

      # O(n log n)
      if chk_idx != -1:
        # 반환받은 값이 중복이면, 인접 값 중에 False인 값을 확인해야함
        if not chk_list[chk_idx]:
          res.append(chk_price)
          chk_list[chk_idx] = True
          cnt += 1

        # 바이너리에서도 chk_list를 확인해서, 그 값이 true인지 확인해야 함

    if cnt == result :
      return res

  return res      

  # # ! set으로 하면, 중복값 사라짐 ! ㅠㅠ
  # res = []
  # chk_set = set(price_list.copy())

  # # O(n)
  # for i in range(len(price_list)-1, -1, -1):   
  #   if price_list[i] % 4 != 0:
  #     continue 

  #   chk_price = int(price_list[i] * (3/4))

  #   # O(1) + O(1)
  #   if chk_price in chk_set:
  #     res.append(chk_price)
  #     chk_set.remove(chk_price)

  #   if len(res) == result :
  #     return res

  # return res

if __name__ == '__main__' :
  tc = int(input())
  
  for i in range(tc):
    result = int(input())
    price_list = list(map(int, input().split()))
    
    # O(n log n)
    ans = find_disCnt_price(result, price_list)
    ans.sort()
    print(f"#{i+1} {' '.join(map(str, ans))}")
    
    # print(f"#{i+1} ", end="")
    # for i in range (len(ans)):
    #   if ans[i]:
    #     print(price_list[i], end=" ")
    # print("")

# O(n^2)를 줄이는 방법
# 

# * TC1
# 2
# 3
# 15 20 60 75 80 100
# 4
# 90 90 120 120 120 150 160 200

# * <<res>>
# * #1 15 60 75
# * #2 90 90 120 150

# * TC2
# 2
# 4
# 15 18 20 21 24 24 28 32
# 5
# 3 4 6 8 9 12 12 15 16 20

# * <<res>>
# * #1 15 18 21 24
# * #2 3 6 9 12 15