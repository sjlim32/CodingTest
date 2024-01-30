# 그래서 진영 주식회사는, 다른 모든 지원자와 비교했을 때 서류심사 성적과 면접시험 성적 중 적어도 하나가 다른 지원자보다 떨어지지 않는 자만 선발한다는 원칙을 세웠다. 
# 즉, 어떤 지원자 A의 성적이 다른 어떤 지원자 B의 성적에 비해 서류 심사 결과와 면접 성적이 모두 떨어진다면 A는 결코 선발되지 않는다.

# 첫째 줄에는 테스트 케이스의 개수 T(1 ≤ T ≤ 20)가 주어진다. 
# 각 테스트 케이스의 첫째 줄에 지원자의 숫자 N(1 ≤ N ≤ 100,000)이 주어진다. 
# 둘째 줄부터 N개 줄에는 각각의 지원자의 서류심사 성적, 면접 성적의 순위가 공백을 사이에 두고 한 줄에 주어진다. 
# 두 성적 순위는 모두 1위부터 N위까지 동석차 없이 결정된다고 가정한다.

# import sys
# input = sys.stdin.readline

# def new_cruit(grade: list) -> int:
#   cut = grade[1]
#   res = 0
#   for paper, meet in enumerate(grade):
#     if paper == 0:
#       continue
    
#     if meet == 1:
#       print('last one', paper, meet)
#       res += 1
#       return res
#     if meet <= cut:
#       print('congratuation', paper, meet)
#       cut = meet
#       res += 1

#   return res

# if __name__ == '__main__':
  
#   tc = int(input())
#   result = []

#   for _ in range(tc):
#     candi = int(input())
#     grade = [ 0 for _  in range(candi +1) ]
#     for _ in range(candi):
#       p, m = map(int, input().split())
#       grade[p] = m
    
#     print(grade)

#   #   result.append(new_cruit(grade))

#   # print(result)

#     print(new_cruit(grade))


## * Optimizing ##
import sys
input = sys.stdin.readline

def new_cruit(num: int, grade: list) -> int:
  cut = grade[1]
  res = 1
  for i in range(2, num+1):
    if grade[i] == 1:
      # print('last one', i, grade[i])
      res += 1
      return res

    if grade[i] <= cut:
      # print('congratuation', i, grade[i])
      cut = grade[i]
      res += 1

  return res

if __name__ == '__main__':
  tc = int(input())

  for _ in range(tc):
    candi = int(input())
    grade = [0] * (candi +1)

    for _ in range(candi):
      p, m = map(int, input().split())
      grade[p] = m

    # print(grade)
    print(new_cruit(candi, grade))