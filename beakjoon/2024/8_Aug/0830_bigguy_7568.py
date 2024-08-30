# 두 사람 A 와 B의 덩치가 각각 (x, y), (p, q)라고 할 때 x > p 그리고 y > q 이라면 우리는 A의 덩치가 B의 덩치보다 "더 크다"고 말한다.
# 두 사람 C와 D의 덩치가 각각 (45, 181), (55, 173)이라면 몸무게는 D가 C보다 더 무겁고, 키는 C가 더 크므로, "덩치"로만 볼 때 C와 D는 누구도 상대방보다 더 크다고 말할 수 없다. ( 공동 순위 )

lst = []
ans = []

for i in range(int(input())):
  weight, height = map(int, input().split())
  lst.append([weight, height])

list = sorted(lst, key=lambda x: x[0], reverse=True)

for man in list:
  print(sum(man))




# Example
# 5
# 55 185
# 58 183
# 88 186
# 60 175
# 46 155

