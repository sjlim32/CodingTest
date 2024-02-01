# import sys
# input = sys.stdin.readline

# if __name__ == '__main__':
#   n = int(input())
#   point = []

#   if n == 0:
#     print(0)

#   elif n == 1:
#     print(int(input()))

#   else:
#     for _ in range(n):
#       point.append(int(input()))

#     dp = [ [0] * n for _ in range(3) ]
#     dp[1][0] = point[0]
#     dp[1][1] = point[1]
#     dp[2][1] = point[0] + point[1]

#     for i in range(2, n):
#       p = point[i]

#       # 전전칸에서 2칸 오른 값
#       dp[0][i] = dp[2][i-1]
#       # 전전칸에서 2칸 오른 값, 또는 전전칸에서 1칸 오른 값
#       dp[1][i] = max(dp[0][i-1] + p, dp[1][i-2] + p)
#       # 전칸에서 1칸 오른 값
#       dp[2][i] = dp[1][i-1] + p

#     print(max(dp[1][n-1], dp[2][n-1]))

## * Optimizing ##
n = int(input())
stairs = [0] + [int(input()) for _ in range(n)]
dp = [0] * (n+1)
dp[1] = stairs[1]

for i in range(2,n+1):
    dp[i] = max(dp[i-3]+stairs[i-1]+stairs[i],dp[i-2]+stairs[i])
print(dp[n])