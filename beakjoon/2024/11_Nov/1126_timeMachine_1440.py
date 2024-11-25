# 시는 01-12
# 분은 00-59
# 초는 00-59

# a, b, c = map(int, input().split(":"))

# if a + b + c or a > 59 or b > 59 or c or 59 == 0:
#   print(0)
# else:
#   ans = 0
#   ans += 2 if 0 < a < 13 else 0
#   ans += 2 if 0 < b < 13 else 0
#   ans += 2 if 0 < c < 13 else 0
#   print(ans)

# OPTIMIZING
a, b, c = map(int, input().split(":"))
if a + b + c == 0 or a > 59 or b > 59 or c > 59:
  print(0)
else:
  print(sum(2 for x in (a, b, c) if 0 < x < 13))

# 두 줄 풀이
# moya=tuple(map(int,input().split(':')))
# print(len(list(filter(lambda y: list(map(lambda x: {True:lambda z:1<=z<=12,False:lambda z:0<=z<=59}[x==y](moya[x]), range(3))).count(True)==3, range(3))))*2)