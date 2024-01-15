# 알파벳 소문자로 이루어진 N개의 단어가 들어오면 아래와 같은 조건에 따라 정렬하는 프로그램을 작성하시오.

# 길이가 짧은 것부터
# 길이가 같으면 사전 순으로
# 단, 중복된 단어는 하나만 남기고 제거해야 한다.

# # 1. 길이순으로 정렬
# import sys
# sys.setrecursionlimit(10**4)

# def q_s(l, left, right):
#   pl = left
#   pr = right
#   pivot = len(l[(left+right) // 2])

#   while pl <= pr:                   # 왼쪽 피벗이 오른쪽 피벗보다 같거나 작으면
#     while len(l[pl]) < pivot: pl += 1       # 현재 pivot 보다 큰 값을 찾을 때까지 왼 피벗을 오른쪽으로 이동
#     while len(l[pr]) > pivot: pr -= 1       # 현재 pivot 보다 작은 값을 찾을 때까지 오른 피벗을 왼쪽로 이동

#     if pl <= pr:
#       l[pl], l[pr] = l[pr], l[pl]   # 왼쪽 피벗이 오른쪽 피벗보다 같거나 작으면 서로 값 교환
#       pl += 1                       # 이후 다른 값 탐색을 위해 피벗을 다음 칸으로 이동
#       pr -= 1
    
#     if left < pr: q_s(l, left, pr)
#     if pl < right: q_s(l, pl, right)  

# # 3. 같은 길이면, 사전순으로 정렬
# def s_d(words):
#   for i in range(len(words)-1):
#     if len(words[i]) == len(words[i]):
#       for a in range(len(words[i])-1):
#         if words[i][a] > words[i+1][a]:
#           words[i], words[i+1] = words[i+1], words[i]    

# # 2. 중복 값 있으면 지움
# words = list(set(input() for _ in range(int(input()))))

# q_s(words, 0, len(words)-1)
# s_d(words)

# print(*words, sep="\n")

##### import sys 전 > 런타임 에러 (recursionError)
##### import sys 후 > 시간초과

# my answer
import sys
words = sorted(set(sys.stdin.readline().strip() for _ in range(int(sys.stdin.readline()))))
words.sort(key=lambda x : len(x))
sys.stdout.write("\n".join(words))


# Optimizing
# import sys
# input = sys.stdin.readline
# print = sys.stdout.write

# cnt = int(input())
# A = []
# for i in range(cnt):
#   A.append(input().strip())

# A = list(set(A))
# A.sort()
# A.sort(key=lambda x: len(x))

# print("\n".join(A))