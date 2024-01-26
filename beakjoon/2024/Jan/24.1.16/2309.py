# 아홉 개의 줄에 걸쳐 난쟁이들의 키가 주어진다. 
# 
# 주어지는 키는 100을 넘지 않는 자연수이며, 아홉 난쟁이의 키는 모두 다르며, 가능한 정답이 여러 가지인 경우에는 아무거나 출력한다.

import sys
input = sys.stdin.readline
# print = sys.stdout.write

heights = [int(input()) for i in range(9)]

def permutation(arr, r):
  ret = []

  def permute(p, index):
    if len(p) == r:
      ret.append(p)
      return

    for idx, height in enumerate(arr):
      if idx not in index:
        permute(p + [height], index + [idx])
  
  permute([], [])
    
  return ret

for ans in permutation(heights, 7):
  if sum(ans) == 100:
    ans.sort()
    print(*ans, sep='\n')
    break;
  
## * Other Answer ##

# 9명의 난쟁이 중 진짜 난쟁이인 7명의 키의 합은 100
# 9명의 키를 모두 더한 뒤 100을 빼면 가짜 난쟁이 두명의 키의 합이 도출
# 0~8번 째 난쟁이 i와 1~9번 째 난쟁이 j 의 키를 합한 경우의 수와 대조, 일치할 때 그 둘을 제외 하고 출력
  
# import sys
# n = [int(sys.stdin.readline()) for _ in range(9)]
# n.sort()
# fake_n = []
# for i in range(8):
#     for j in range(i+1, 9):
#         if n[i]+n[j] == sum(n) - 100:
#             fake_n.append(n[i])
#             fake_n.append(n[j])
#     if fake_n:
#         break
# n.remove(fake_n[0])
# n.remove(fake_n[1])

# for i in n:
#     print(i)