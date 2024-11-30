# ans = []

# while(True):
#   n = int(input())
#   queto = []
#   if n == 0:
#     break
  
#   queto = [input()for _ in range(n)]

#   goal = 0

#   for i,se in enumerate(queto):
#     new_space = 0

#     if len(queto) == 1:
#       goal = (len(queto[0]) + 1)
#       break
    
#     if i == 0:
#       goal += 1
#       bef_char = se[0]
#       for i, char in enumerate(se[1:]):
#         goal += 1
#         if bef_char != ' ' and char == ' ':
#           break
#         bef_char = char
#         if i == len(se) -2:
#           goal += 1
#           break
#     else:
#       for i, char in enumerate(se):
#         new_space += 1
#         if char == ' ' and new_space >= goal:
#           goal = new_space
#           break
#         if i == len(se) -1 and new_space >= goal:
#           goal = new_space + 1
#           break
        
#   ans.append(goal)

# for i in ans:
#   print(i)

# OPTIMIZING
import sys
input=sys.stdin.readline
while(True):
  n=int(input())
  if(n==0):break
  b=0
  for i in range(n):
    a=input()
    for j in range(b,len(a)):
      if(j==0):continue
      if(a[j-1]!=" " and a[j]==" "):
        b=j
        break
      else:b=len(a)-1
  print(b+1)