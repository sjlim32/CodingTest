
# 한 개의 회의실이 있는데 이를 사용하고자 하는 N개의 회의에 대하여 회의실 사용표를 만들려고 한다. 
# 각 회의 I에 대해 시작시간과 끝나는 시간이 주어져 있고, 각 회의가 겹치지 않게 하면서 회의실을 사용할 수 있는 회의의 최대 개수를 찾아보자.

# 첫째 줄에 회의의 수 N(1 ≤ N ≤ 100,000)이 주어진다.
# 둘째 줄부터 N+1 줄까지 각 회의의 정보가 주어지는데 이것은 공백을 사이에 두고 회의의 시작시간과 끝나는 시간이 주어진다. 
# 시작 시간과 끝나는 시간은 2^31-1보다 작거나 같은 자연수 또는 0이다.

import sys
input = sys.stdin.readline

def booker():
  meeting = int(input())
  table = []
  res = 0
  for _ in range(meeting):
    s, e = map(int, input().split())
    table.append([s, e])

  if meeting == 1:
    print(1)
  else:
    table.sort(key = lambda x: (x[1], x[0]))

    for i in range(1, meeting):
      if res == 0:
        now = table[0]
        res += 1

      if now[1] > table[i][0]:
        continue
      else:
        res += 1
        now = table[i]
  
  return res

if __name__== "__main__" :
  print(booker())


## * Optimizing ##

# import sys
# input = sys.stdin.readline

# def main():
#   meeting = int(input())
#   table = []

#   for _ in range(meeting):
#     s, e = map(int, input().split())
#     table.append((e, s))

#   table.sort()
#   end_time, _ = table[0]
#   res = 1
#   for end, start in table[1:]:
#     if start >= end_time:
#       end_time = end
#       res += 1
  
#   return res

# if __name__== "__main__" :
#   print(main())
