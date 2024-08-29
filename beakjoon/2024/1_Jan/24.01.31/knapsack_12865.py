# 준서가 여행에 필요하다고 생각하는 N개의 물건이 있다. 
# 각 물건은 무게 W와 가치 V를 가지는데, 해당 물건을 배낭에 넣어서 가면 준서가 V만큼 즐길 수 있다. 
# 아직 행군을 해본 적이 없는 준서는 최대 K만큼의 무게만을 넣을 수 있는 배낭만 들고 다닐 수 있다. 
# 준서가 최대한 즐거운 여행을 하기 위해 배낭에 넣을 수 있는 물건들의 가치의 최댓값을 알려주자.

# 첫 줄에 물품의 수 N(1 ≤ N ≤ 100)과 
# 준서가 버틸 수 있는 무게 K(1 ≤ K ≤ 100,000)가 주어진다. 
# 두 번째 줄부터 N개의 줄에 거쳐 각 물건의 무게 W(1 ≤ W ≤ 100,000)와 
# 해당 물건의 가치 V(0 ≤ V ≤ 1,000)가 주어진다.

# import sys
# input = sys.stdin.readline

# def knap(n: int, k: int, items: list) -> int:
#   dp = [ [0] * (k + 1) for _ in range(n) ]
#   items.sort()  

#   for i in range(n):
#     for l in range(k + 1):
#       w, v = items[i]

#       if w > l:
#         # print('not in', i, l)
#         dp[i][l] = dp[i-1][l]

#       else:
#         # print('in', i, l)
#         dp[i][l] = max(dp[i-1][l], dp[i-1][l-w] + v)
#         # print('now', dp[i][l])
#   return dp[n-1][l]

# if __name__ == '__main__':
#   n, k = map(int, input().split())
#   items = []
#   for _ in range(n):
#       w, v = map(int, input().split())
#       items.append([w, v])

#   res = 0
#   if n == 1 and k > w:
#     res = items[0][1]
#   elif n == 1 and k < w:
#     res = 0
#   else:
#     res = knap(n, k, items)

#   print(res)

## * Optimizing ##
import sys; input = sys.stdin.readline

def main():
    n, k = map(int, input().split())
    k += 1

    bag = {0: 0}
    data = [tuple(map(int,input().split())) for _ in range(n)]
    data.sort(reverse=True)

    for w, v in data:
        tmp = {}
        for v_bag, w_bag in bag.items():
            # bag을 순회, (넣어야 하는 v + 가방의 v를 더한 값)이 가방에 들어있는지 확인
            # 있으면 그 값의 w 와, (넣어야하는 w + 가방의 w)를 비교해서 후자가 작으면 temp 업데이트
            # 없으면 가방의 한도(k) 와 넣어야하는 w + 가방의 w를 비교헤서 후자가 작으면 temp 업데이트
            if bag.get(nv := v + v_bag, k) > (nw := w + w_bag):
                tmp[nv]=nw
        # temp에 담긴 경우의 수를 모두 가방에 넣음
        bag.update(tmp)

    # 가방의 한도 중 가장 큰 데이터를 불러옴
    print(max(bag.keys()))

main()