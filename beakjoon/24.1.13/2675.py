# 문자열 S를 입력받은 후에, 각 문자를 R번 반복해 새 문자열 P를 만든 후 출력하는 프로그램을 작성하시오. 

testcase = int(input())
ans = []

while True:
  if len(ans) == testcase:
    break;

  tc_list = []
  input_str = input().split()

  for i in range(len(input_str[1])):
    tc_list.append(input_str[1][i]*int(input_str[0]))
  ans.append(''.join(tc_list))

for i in range(testcase):
  print(ans[i])


# iStr = input().split()
# if len(iStr) > 1:
#   rep, let = iStr
#   ans = []
#   for i in range(len(let)):
#     ans.append(let[i]*int(rep))
#   print(''.join(ans))
# else:
#   end;

# iStr = input().split()
# if len(iStr) > 1:
#   rep, let = iStr
#   for i in range(len(let)):
#     print(let[i]*int(rep), end='')


# inputStr = input()
# sepStr = inputStr.split()
# ans = []

# if len(sepStr) > 1:
#   for i in range(len(sepStr[1])):
#     ans.append(sepStr[1][i]*int(sepStr[0]))
#   print(''.join(ans))  


## * Optimizing ##

# tc = int(input())

# for i in range(tc):
#   r, s = input().split()
#   for i in range(len(s)):
#     print(s[i]*int(r), end='')
#   print()
