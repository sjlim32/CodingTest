# 먼저 주어진 수가 10보다 작다면 앞에 0을 붙여 두 자리 수로 만들고, 각 자리의 숫자를 더한다. 
# 그 다음, 주어진 수의 가장 오른쪽 자리 수와 앞에서 구한 합의 가장 오른쪽 자리 수를 이어 붙이면 새로운 수를 만들 수 있다. 
# N이 주어졌을 때, 원래 수로 돌아오는 N의 사이클의 길이를 구하는 프로그램을 작성하시오.

# 26 4
# 55 3
# 1 60
# 0 1
# 71 12
import sys
input = sys.stdin.readline
print = sys.stdout.write

first = int(input())

def cal(n, cnt):    
  if n == 0:
    print("1")  
    return None

  q = n // 10 
  r = n % 10 
  next_n = r*10+((q + r) % 10)
  cnt += 1
  # print("q, r, next_n", q, r, next_n)
  if next_n == first: 
    print(str(cnt))
  else : 
    cal(next_n, cnt)

cal(first, 0)

## * Optimizing ##
# import sys
# num = int(sys.stdin.readline())
# a = num
# ans = -1

# cnt = 0
# # 같을때까지 반복하기
# while ans != num:
#     front = int(a / 10)
#     behind = a % 10
#     temp = front + behind
#     ans = behind * 10 + (temp % 10)

#     cnt += 1
#     a = ans

# print(cnt)