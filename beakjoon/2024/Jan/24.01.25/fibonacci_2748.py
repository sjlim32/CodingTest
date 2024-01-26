# 피보나치 수는 0과 1로 시작한다. 
# 0번째 피보나치 수는 0이고, 1번째 피보나치 수는 1이다. 그 다음 2번째 부터는 바로 앞 두 피보나치 수의 합이 된다.
# 이를 식으로 써보면 Fn = Fn-1 + Fn-2 (n ≥ 2)가 된다.

# n=17일때 까지 피보나치 수를 써보면 다음과 같다.
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597

# n이 주어졌을 때, n번째 피보나치 수를 구하는 프로그램을 작성하시오.

## ? 메모이제이션 활용

n = int(input())
dp = [ 0 for _ in range(n-1) ]

def fibonacci(n):
  result = 0
  if n < 2:
    return n
  
  else:
    i = n - 2
    if dp[i] != 0:
      result = dp[i]
    else:
      dp[i] = fibonacci(n-2) + fibonacci(n-1)
      result = dp[i]
  
  return result

print(fibonacci(n))

## * Optimizing 2 ##
# n = int(input())
# dp = [ 0 for _ in range(n + 1) ]
# dp[0] = 0
# dp[1] = 1

# for i in range(2, n+1):
#     dp[i] = dp[i-2] + dp[i-1]

# print(dp[n])


## * Optimizing ##
a,b=0,1
for _ in range(int(input())-1):
    a,b=b,a+b
print(b)