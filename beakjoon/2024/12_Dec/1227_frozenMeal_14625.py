# 같은 시간일 때, 시작분부터 끝나는 분까지만 계산
# 다른 시간일 때, 계속 반복 후에, 마지막 반복에서는 끝나는 분까지만 계산

# 같은 시간일 때
# start_m 에 target 포함되는지 확인 ( 두자릿수는 둘 다 확인 ) -> start += 1
# start_m이 end_m 보다 커지면 탈출
# target이 0 일때 = end_m - start_m

# 다른 시간일 때
# start_h가 end_h 보다 커지면 탈출
# 시작 시간일 경우 59 - start_m 만큼만 반복
# 끝나는 시간일 경우 0 ~ end_m 만큼만 반복

def comp(t: int, h:int, m: int) -> int:
  hour = f"{h:02}"  
  minute = f"{m:02}"
    
  if str(t) in hour or str(t) in minute:
      return 1
  return 0

sh, sm = map(int, input().split())
eh, em = map(int, input().split())
target = int(input())
ans = 0

if eh == sh:
  minute = sm
  if sm <= em:
    for minute in range(sm, em + 1):
        ans += comp(target, sh, minute)

else:
  for minute in range(sm, 60):
    ans += comp(target, sh, minute)

  for hour in range(sh + 1, eh):
    for minute in range(60):
      ans += comp(target, hour, minute)

  for minute in range(0, em + 1):
    ans += comp(target, eh, minute)

print(ans)

# OPTIMIZING
bh,bm=map(int,input().split())
ah,am=map(int,input().split())
n=int(input())

cnt=0

while 1:        
    if bh//10==n or bh%10==n or bm//10==n or bm%10==n:
        cnt+=1
    
    if bh==ah and bm==am:
        break

    bm+=1

    if bm>=60:
        bh+=1
        bm%=60

print(cnt)