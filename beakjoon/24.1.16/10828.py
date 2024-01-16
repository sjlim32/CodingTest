# 정수를 저장하는 스택을 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.

# push X: 정수 X를 스택에 넣는 연산이다.
# pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 스택에 들어있는 정수의 개수를 출력한다.
# empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
# top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.

import sys
input = sys.stdin.readline

cl_l = [input().split() for _ in range(int(input()))]
stack = []

for i in range(len(cl_l)):
  cmd, *num = cl_l[i]

  if cmd == 'push':
    stack.append(int(*num))

  elif cmd == 'pop':
    print(stack.pop()) if stack else print(-1)

  elif cmd == 'size':
    print(len(stack))

  elif cmd == 'empty':
    print(0) if stack else print(1)

  elif cmd == 'top':
    print(stack[-1]) if stack else print(-1)


## ? Improve Code Readability ##
# import sys
# input = sys.stdin.readline
# # print = sys.stdout.write
# print = lambda x:sys.stdout.write(x + "\n")

# num = int(input())
# stack = []

# for _ in range(num):
#   cmd=input().rstrip()
#   if cmd == 'pop':
#     print(stack.pop() if stack else "-1")
#   elif cmd == 'size':
#     print(str((len(stack))))
#   elif cmd == 'empty':
#     print("0" if stack else "1")
#   elif cmd == 'top':
#     print(str(stack[-1]) if stack else "-1")
#   else:
#     stack.append(cmd.split()[1])

## * Optimizing ##
# import sys
# input = sys.stdin.readline
# print = sys.stdout.write

# num = int(input())
# stack = []

# for _ in range(num):
#   cmd=input().rstrip()

#   if cmd == 'pop':
#     print(stack.pop()+"\n") if stack else print("-1\n")

#   elif cmd == 'size':
#     print(str((len(stack)))+"\n")

#   elif cmd == 'empty':
#     print("0\n") if stack else print("1\n")

#   elif cmd == 'top':
#     print(str(stack[-1])+"\n") if stack else print("-1\n")
  
#   else:
#     stack.append(cmd.split()[1])