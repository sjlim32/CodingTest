# 준규는 자신의 생활 패턴을 분석하여, 자기가 사용하고 있는 전기용품의 사용순서를 알아내었고, 
# 이를 기반으로 플러그를 빼는 횟수를 최소화하는 방법을 고안하여 보다 쾌적한 생활환경을 만들려고 한다.

# 첫 줄에는 멀티탭 구멍의 개수 N (1 ≤ N ≤ 100)과 전기 용품의 총 사용횟수 K (1 ≤ K ≤ 100)가 정수로 주어진다. 
# 두 번째 줄에는 전기용품의 이름이 K 이하의 자연수로 사용 순서대로 주어진다. 
# 
# 각 줄의 모든 정수 사이는 공백문자로 구분되어 있다.
import sys
input = sys.stdin.readline
from collections import deque

# def find_long_t(items: list, remove_tap = set()) -> int:
#   for item in items:
#     if s_list.index(item) == 0:
#       now_tap.remove(item)
#       return

#     else:remove_tap.add(s_list.index(item))
#   print('r_tap', remove_tap)
#   now_tap.pop(max(remove_tap))

# tap, num = map(int, input().split())
# schedule_list = list(map(int, input().split()))
# print(s_list)

# # schadule = [s_list[i:i+tap] for i in range(0, num, tap)]

  # next_turn = defaultdict(int)
  # for i in (set_l):
  #   next_turn[i] = s_list.index(i)

  # set_l = set(s_list)

# # print(next_turn)
if __name__ == "__main__":

  tap, turn = map(int, input().split())
  schedule_list = list(map(int, input().split()))
  q = deque(schedule_list)
  mult = []
  
  res = 0

  while q:
    nitem = q.popleft()

    # 멀티탭이 비어있을 때
    if len(mult) < tap:
      if nitem not in mult:
        mult.append(nitem)

    # 멀티탭이 꽉 찼는데, 새로운 전자기기를 써야할 때
    else:
      if nitem not in mult:
        remover = 0
        r_id = -1

        # 전자기기 제거하기
        for item in mult:
          # 멀티탭의 전자기기 중 더 이상 사용하지 않을 것 제거
          if item not in q:
            # mult.remove(item)
            remover = item
            break
          
          # 멀티탭의 전자기기 중 가장 남은 턴이 긴 걸 제거 대상으로 변경
          if item in q:
            last_id = q.index(item)
            if last_id > r_id:
              r_id = last_id
              remover = item
        
        # for문을 빠져나왔는데, 멀티탭에 전자기기 중에 필요없는 것이 없을 때,
        # 위에서 선정한 전자기기 하나 제거
        mult.remove(remover)
        res += 1

        if len(mult) != tap:
          mult.append(nitem)
        
  print(res)

  
          #     else:
          #   # 위의 for문에서 제거하지 못했을 때,
          #   remover = 0
          #   for item in mult:
          #     if q.index(item) > remover:
          #       remover = item
          #       print('compare deleted', remover)
          # mult.remove(remover)
          # res += 1
          # mult.append(nitem)

          #           if item not in q:
          #   print('this item is deleting', item)
          #   mult.remove(item)
          #   res +=1
          #   continue