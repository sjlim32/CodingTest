# 오늘부터 N+1일째 되는 날 퇴사를 하기 위해서, 남은 N일 동안 최대한 많은 상담을 하려고 한다.
# 상담을 적절히 했을 때, 백준이가 얻을 수 있는 최대 수익을 구하는 프로그램을 작성하시오.

# 첫째 줄에 N (1 ≤ N ≤ 15)이 주어진다.
# 둘째 줄부터 N개의 줄, Ti와 Pi가 공백으로 구분, 1일부터 N일까지 순서대로 주어진다. 
# 1 ≤ Ti ≤ 5      //    1 ≤ Pi ≤ 1,000




n = int(input())
table = []

for _ in range(n):
  t, v = map(int, input().split())
  table.append([t, v])

dp = [ [0] * (n + 1) for _ in range(n) ]

for i in range(n):
  for j in range(n + 1):
    t, v = table[i]

    if i + t == j:
      dp[i][j] = max(dp[i - 1][j - t] + v, dp[i - 1][j])
      
    else:
      dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

sprint(max(dp[n-1]))

# n = int(input())
# table = []

# for _ in range(n):
#   t, v = map(int, input().split())
#   table.append([t, v])

# dp = [0] * (n + 1)

# for i in range(n):
#   t, v = table[i]

#   if i + t <= n:
#     dp[i + t] = max(dp[i] + v, dp[i + t], dp[i-1])

# print(max(dp))

## * Optimizing ##
# n = int(input())

# dp = [0] * (n+1)

# case = []

# for _ in range(n):
#     t, p = map(int, input().split())
#     case.append((t, p))


# for idx, c in enumerate(case, start=1):
#     for i in range(idx+c[0]-1, n+1):
#         dp[i] = max(dp[i], dp[idx-1] + c[1])

# print(dp[-1])