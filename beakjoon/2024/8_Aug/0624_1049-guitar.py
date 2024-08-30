
#* 첫째줄 (끊어진 기타줄, 기타줄 브랜드) = N, M // N <= 100, M <= 50
#? 둘째줄부터 M개의 줄까지 = 6개 패키지의 가격, 낱개 가격
#? 기타줄 최소 N개를 필요로 할 때, 드는 돈의 최소값을 출력


# 끊어진 기타줄이 6 이하일 때, 
# 1. 첫번째 값이 가장 작은 것 찾음
# 2. 낱개 가격이 가장 작은 것 찾음
# 3. 6묶음의 배수 vs 6묶음 + 낱개 중 싼 것 선택
# 4. 낱개 * 갯수

import sys

input = sys.stdin.readline

if __name__ == "__main__" :
  
  cut_lines, brands = map(int, input().split())
  min_bundle = sys.maxsize
  min_unit = sys.maxsize

  for r in range(brands):
    bundle, unit = map(int, input().split())
    min_bundle = bundle if bundle < min_bundle else min_bundle
    min_unit = unit if unit < min_unit else min_unit

  quotient, remainder = divmod(cut_lines, 6)
  bundle_price = min_bundle * (quotient + 1)
  include_unit_price =  (min_bundle * quotient) + min_unit * remainder
  only_unit_price = min_unit * cut_lines
  ans = bundle_price if bundle_price < include_unit_price else include_unit_price
  ans = only_unit_price if only_unit_price < ans else ans

  print(ans)


######* OPTIMIZING *######
lines, brands = map(int, input().split())
list = []
for r in range(brands):
  list.extend(map(int, input().split()))

pack, prc = min(list[::2]), min(list[1::2])

print(min(pack * ((lines - 1) // 6 + 1), (pack * (lines // 6 )) + prc * (lines % 6), prc * lines))

# example
# 4 2
# 12 3
# 15 4

# 9 16
# 21 25
# 77 23
# 23 88
# 95 43
# 96 19
# 59 36
# 80 13
# 51 24
# 15 8
# 25 61
# 21 22
# 3 9
# 68 68
# 67 100
# 83 98
# 96 57