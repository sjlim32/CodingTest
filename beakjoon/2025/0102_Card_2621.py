# R, B, Y, G / 1-9
# 36장 중에 5장의 카드가 주어짐

# 스트레이트 플러시 - 900점 + 가장 높은 숫자
# 포카드 - 800점 + 같은 숫자
# 풀하우스 - 700장 + 3장 숫자 * 10 + 2장 숫자
# 플러시 - 600 + 가장 높은 숫자
# 스트레이트 - 500 + 가장 높은 숫자
# 트리플 - 400 + 가장 높은 숫자
# 투페어 - 300 + 큰 숫자 * 10 + 작은 숫자
# 원페어 - 200 + 같은 숫자
# 노페어 - 100 + 가장 큰 숫자

from collections import Counter

def sol(hand: list):

    colors = [c for c, n in hand]
    numbers = [n for c, n in hand]

    color_count = Counter(colors)
    num_count = Counter(numbers)
    sorted_nums = sorted(numbers)

    is_flush = (max(color_count.values()) == 5)

    is_straight= True
    for i in range(4):
       if sorted_nums[i+1] - sorted_nums[i] != 1:
          is_straight = False
          break
    highest_straight = sorted_nums[-1]

    # 포카드 ~ 노페어
    num_freq = sorted(num_count.items(), key=lambda x: (x[1], x[0]), reverse=True)
    first_num, first_count = num_freq[0]
    if len(num_freq) > 1:
      second_num, second_count = num_freq[1]
    else:
       second_num, second_count = 0, 0

    if is_flush and is_straight:
       return 900 + highest_straight
    elif first_count >= 4:
       return 800 + first_num
    elif first_count == 3 and second_count == 2:
       return 700 + second_num + (first_num * 10)
    elif is_flush:
       return 600 + max(numbers)
    elif is_straight:
       return 500 + highest_straight
    elif first_count == 3:
       return 400 + first_num
    elif first_count == 2 and second_count == 2:
       return 300 + second_num + (first_num * 10)
    elif first_count == 2:
       return 200 + first_num
    else:
       return 100 + max(numbers)

if __name__ == "__main__":
  hand = []

  for i in range(5):
    color, num = input().split()
    hand.append((color, int(num)))

  print(sol(hand))

# OPTIMIZING  

conv = lambda x: int(x) if x.isnumeric() else x # isnumeric() = 문자열 형태의 숫자인지 확인 맞으면 True 반환

color = []
num = []
for _ in range(5):
    c, n = map(conv, input().strip().split())
    color.append(c)
    num.append(n)
num.sort()

cnt = [[] for _ in range(6)]
for n in list(set(num)):
    cnt[num.count(n)].append(n) # 중복을 제거한 n값을 바탕으로 num 갯수가 cnt의 인덱스가 되도록 리스트에 넣음
seq = len(set(num)) == 5 and max(num) - min(num) == 4 # 중복없이 5개의 숫자가 존재하고, 최대값과 최소값의 차이가 4이면 스트레이트임

ans = 0
if len(set(color)) == 1 and seq:
    ans = max(num) + 900  
elif len(set(num)) == 2 and cnt[4]:
    ans = 800 + cnt[4][0]
elif len(set(num)) == 2 and cnt[3] and cnt[2]:
    ans = cnt[3][0] * 10 + cnt[2][0] + 700
elif len(set(color)) == 1:
    ans = max(num) + 600
elif seq:
    ans = max(num) + 500
elif len(set(num)) == 3 and cnt[3]:
    ans = cnt[3][0] + 400
elif len(cnt[2]) == 2:
    ans = max(cnt[2]) * 10 + min(cnt[2]) + 300
elif cnt[2]:
    ans = cnt[2][0] + 200
else:
    ans = max(num) + 100
print(ans)