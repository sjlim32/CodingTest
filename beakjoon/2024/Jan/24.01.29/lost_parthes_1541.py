# 세준이는 양수와 +, -, 그리고 괄호를 가지고 식을 만들었다. 그리고 나서 세준이는 괄호를 모두 지웠다.
# 그리고 나서 세준이는 괄호를 적절히 쳐서 이 식의 값을 최소로 만들려고 한다.
# 괄호를 적절히 쳐서 이 식의 값을 최소로 만드는 프로그램을 작성하시오.

# 첫째 줄에 식이 주어진다. 
# 식은 ‘0’~‘9’, ‘+’, 그리고 ‘-’만으로 이루어져 있고, 가장 처음과 마지막 문자는 숫자이다. 
# 그리고 연속해서 두 개 이상의 연산자가 나타나지 않고, 5자리보다 많이 연속되는 숫자는 없다. 
# 수는 0으로 시작할 수 있다. 
# 입력으로 주어지는 식의 길이는 50보다 작거나 같다.

# import re
# formula = input()
# fList = re.split('[+-]', formula)
import sys

formula = sys.stdin.readline().rstrip()
# print(formula)

if '-' in formula:
  fList = formula.split('-')
  # print(fList)

  for i in range(len(fList)):
      if '+' in fList[i]:
        cal = fList[i].split('+')
        cal = list(map(lambda x: int(x.lstrip('0')), cal))
        # print(cal)
        fList[i] = sum(cal)
  
  r_list = list(map(int, fList))
  # print('next', r_list)

  for i in range(len(r_list)-1):
    # print(i)
    r_list[i+1] = r_list[i] - r_list[i + 1]
    # print('res',r_list[i+1])
    if i == (len(r_list)-2):
      sys.stdout.write(str(r_list[i+1]))
  # print(r_list)
  # min_v = min(r_list)
  # print(min_v)
  # sys.stdout.write(f'{(min_v - (sum(r_list)- min_v))}')
    
else:
  fList = formula.split('+')
  r_list = list(map(int, fList))
  # print(r_list)
  sys.stdout.write(f'{sum(r_list)}')


## * Optimizing ##
# exp = input().split('-')
# num = []
# for i in exp:
#     cnt = 0
#     sum = i.split('+')
#     for j in sum:
#         cnt += int(j)
#     num.append(cnt)
# ans = num[0]
# for i in range(1, len(num)):
#     ans -= num[i]
# print(ans)