# 0보다 크거나 같은 정수 N이 주어진다. 이때, N!을 출력하는 프로그램을 작성하시오.

def fact(n):
  if n <= 1:
    return 1
  return n * fact(n-1)

n = int(input())
print(fact(n))


## Other Answer ##

# N=1
# for i in range(int(input()), 1, -1):
#   N = N * 1
# print(N)