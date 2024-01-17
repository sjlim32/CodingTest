# N과 K가 주어지면 (N, K)-요세푸스 순열을 구하는 프로그램을 작성하시오.

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

# 사람수 = n
# 리스트 = people
# 순번 = k
# 순번카운트 = cnt

n, k = map(int, input().split())
people = list(range(1, n+1))
ans = []

def kill_i(last_p, cnt):

  if len(last_p) < 2:
    if last_p:
      ans.append(last_p[0])
      return None
    else:
      return None

  die_list = []
  count = cnt

  for i in range(len(last_p)):
    print("last_people, order", last_p, i)
    count -= 1

    if count == 0:
      die_list.append(last_p[i])
      print("Kill!:", last_p[i])
      count = k
    # else:

  for die in die_list:
    ans.append(die)
    last_p.remove(die)

  print("last count:", count)
  kill_i(last_p, count)

while True:
  if n == 1:
    print('<1>')
    break;
  elif len(people) < 2:
    answer = ', '.join(str(n) for n in ans)
    print(f"<{answer}>")
    break;
  else:
    kill_i(people, k)


## * Optimizing ##
# N, K = input().split()

# N = int(N)
# K = int(K)
# cnt = 0

# list = [i + 1 for i in range(N)]
# print("<", end="")

# while list:
#     cnt = (cnt + K - 1) % len(list)
#     if len(list) != 1:
#         print(list[cnt], end=", ")
#     else:
#         print(list[cnt], end="")
#     list.remove(list[cnt])

# print(">", end="")
  