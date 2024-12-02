n, plnt = map(int, input().split())
univ = [list(map(int, input().split())) for _ in range(n)]


ans = 0
for i in range(n-1):
  for j in range(i + 1, n):
    cnt = 0
    for k in range(plnt):
      if univ[i][k-1] > univ[i][k] and univ[j][k-1] > univ[j][k]:
        cnt += 1
      if univ[i][k-1] < univ[i][k] and univ[j][k-1] < univ[j][k]:
        cnt += 1
      if univ[i][k-1] == univ[i][k] and univ[j][k-1] == univ[j][k]:
        cnt += 1
    
    if cnt == plnt:
      ans += 1 
        
print(ans)

# OPTIMIZING
# 각 값을 크기 별로 정렬 후 정규화 진행, 이후 정규화 된 행간 비교로 결과값 산출
import sys
m,n=map(int,sys.stdin.readline().split())
universe = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]

for arr in universe:
    tmpList=sorted(list(set(arr)))
    tmpDic={tmpList[i]:i for i in range(len(tmpList))}
    for j in range(len(arr)):
        arr[j]=tmpDic[arr[j]]

count=0
for i in range(m-1):
    for j in range(i+1,len(universe)):
            if universe[i]==universe[j]:
                count+=1
print(count)