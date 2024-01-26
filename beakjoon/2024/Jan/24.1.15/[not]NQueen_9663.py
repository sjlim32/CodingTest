# N-Queen 문제는 크기가 N × N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제이다.

# N이 주어졌을 때, 퀸을 놓는 방법의 수를 구하는 프로그램을 작성하시오.
# https://gamedevlog.tistory.com/56

## 체스 보드 그리기
# n = int(input())
# board = [[True for w in range(n)] for h in range(n)]

# def board_printer():
#   for i in range (len(board)):
#     print(board[i])
# board_printer()


##### -----
# n = int(input())
# board = [[True for w in range(n)] for h in range(n)]



# for l in range(n):
#   for s in range(n):

#     if board[l][s] == True:
#       board[l][s] = "queen"
#                                   # if board[3,2]
#       for i in range(n-l-1):          # if n 6 : 0, 1, 2, 3, 4, 5  >> n= 6 - 3 : 0, 1, 2
#         board[l+i][s+i] = False      # 정대각선 False  [4,3] , [5,4]
#         # board[l+i][i-s] = False
#         # board[l+i][s] = False       # 같은 열 False
#         # board[l][s+i] = False       # 같은 행 False
##### -----

# c =2 , r = 4, n =6
def conq(c, r, n) :          
  conq_list = []
  print(c, r, n)

  for yx in zip(c, r):
    conq_list.append(yx)



conq(2, 4 ,6)
