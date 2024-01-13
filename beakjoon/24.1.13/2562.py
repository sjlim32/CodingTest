# 9개의 서로 다른 자연수가 주어질 때, 이들 중 최댓값을 찾고 그 최댓값이 몇 번째 수인지를 구하는 프로그램을 작성하시오.
nums = []
while len(nums) < 9:
  nums.append(int(input()))

print(f"{max(nums)}\n{nums.index(max(nums))+1}")
# print(max(nums))
# print(nums.index(max(nums)))

## Optimizing ##
# nums=[int(input()) for i in range(9)]

