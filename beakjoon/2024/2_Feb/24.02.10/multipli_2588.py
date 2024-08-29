# (세 자리 수) × (세 자리 수)는 다음과 같은 과정을 통하여 이루어진다.
# 입력
# 첫째 줄에 (1)의 위치에 들어갈 세 자리 자연수가, 둘째 줄에 (2)의 위치에 들어갈 세자리 자연수가 주어진다.

# 출력
# 첫째 줄부터 넷째 줄까지 차례대로 (3), (4), (5), (6)에 들어갈 값을 출력한다.

n = int(input())
m = [int(d) for d in input()]
digit = int("".join(map(str,m)))

print(f"{n*m[2]}\n{n*m[1]}\n{n*m[0]}\n{n*digit}\n")

## * Optimizing ##
# a,b = int(input()),input()
# print(*[a*int(p) for p in b][::-1], a*int(b))