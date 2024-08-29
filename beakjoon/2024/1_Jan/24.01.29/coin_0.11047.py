# 준규가 가지고 있는 동전은 총 N종류이고, 각각의 동전을 매우 많이 가지고 있다.

# 동전을 적절히 사용해서 그 가치의 합을 K로 만들려고 한다. 이때 필요한 동전 개수의 최솟값을 구하는 프로그램을 작성하시오.

# 첫째 줄에 N과 K가 주어진다. 
# 1 ≤ N ≤ 10
# 1 ≤ K ≤ 100,000,000

# 둘째 줄부터 N개의 줄에 동전의 가치 Ai가 오름차순으로 주어진다. 
# 1 ≤ Ai ≤ 1,000,000
# A1 = 1, i ≥ 2인 경우에 Ai는 Ai-1의 배수

import sys

def nums_of_coin(price: int, coin_list: list) -> int:
  res = 0
  # while price != 0:
  #   for i in range(len(coin_list) -1, -1, -1):
  #     coin = coin_list[i]
      
  #     if price < coin:
  #       continue
  #     else:
  #       price -= coin
  #       res += 1

  #       if price == 0:
  #         return res

  #       break

  # for i in range(r-1, -1, -1):
    # coin = coin_list[i]
  for coin in coin_list:  
    if price >= coin :
      res += price // coin
      price = price % coin

      if price == 0:
        return res
    
    else:
      continue


if  __name__ == "__main__":
  r, cost = map(int, sys.stdin.readline().split())
  vari = []
  for _ in range(r):
    vari.append(int(sys.stdin.readline()))
  
  vari.reverse()
  print(vari)

  sys.stdout.write(str(nums_of_coin(cost, vari)))


## * Optimizing ##

# import sys

# t,p = map(int,input().split())
# ll = []
# for i in range(t):
#   ll.append(int(sys.stdin.readline()))
# count = 0
# for k in range(t-1,-1,-1):

#   if p//ll[k]>0:
#     count+=p//ll[k]
#     p = p%ll[k]
#   else:
#     continue

# print(count)