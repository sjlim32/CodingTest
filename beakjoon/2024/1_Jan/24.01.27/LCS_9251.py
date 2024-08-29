# LCS(Longest Common Subsequence, 최장 공통 부분 수열)문제는 두 수열이 주어졌을 때, 
# 모두의 부분 수열이 되는 수열 중 가장 긴 것을 찾는 문제이다.
# 예를 들어, ACAYKP와 CAPCAK의 LCS는 ACAK가 된다.

# 첫째 줄과 둘째 줄에 두 문자열이 주어진다. 
# 문자열은 알파벳 대분자로, 최대 1000글자

# 첫째줄에 입력으로 주어진 두 문자열의 LCS 길이를 출력
import sys
sys.setrecursionlimit(10**6)

## ? 공통부분 "문자열 "을 출력하는 방법
def LCS(y: int, x: int, result: list = []) -> list :
  if y < 0 or x < 0:
    return

  else:  
    if DP[y][x] == DP[y-1][x] and y > 0:
      LCS(y - 1, x, result)

    elif DP[y][x] == DP[y][x-1] and x > 0:
      LCS(y, x - 1, result)

    else:
      if DP[y][x] != 0:
        result.append(str1[y-1])

      if DP[y - 1][x - 1] != 0:
        LCS(y - 1, x - 1, result)
      
      else:
        result.reverse()
        return result

  result.reverse()
  return result


## ? 공통 부분 "문자열의 길이"를 출력하는 방법
if __name__ == "__main__":
  str1 = input()
  str2 = input()
  n = len(str1)
  m = len(str2)

  DP = [[0] * (m + 1) for _ in range(n + 1)]

  # print(DP)

  for i in range(1, n+1):
    for j in range(1, m+1):
      DP[i][j] = DP[i - 1][j - 1] + 1 if str1[i-1] == str2[j-1] else max(DP[i - 1][j], DP[i][j - 1])
  
      # if str1[i - 1] == str2[j - 1]:
      #   DP[i][j] = DP[i - 1][j - 1] + 1 
      # else:
      #   DP[i][j] = max(DP[i - 1][j], DP[i][j - 1])

  print(max(max(DP)))
  # res = ''.join(LCS(n, m))
  # print(res)
  # print(len(LCS(n, m)))

## * Optimizing
## ? 메모리를 사용하지 않고 가장 긴 문자열의 길이만 간단하게 출력
# import sys
# input = sys.stdin.readline
# X = input().rstrip()
# Y = input().rstrip()

# def answer(X, Y) :
# 	DP = [0] * 1000

# 	for i, x in enumerate(X):
# 		cnt = 0
# 		for j, y in enumerate(Y):
# 			if cnt < DP[j]:
# 				cnt = DP[j]
# 			elif x == y:
# 				DP[j] = cnt + 1
	
# 	return max(DP)

# print(answer(X, Y))