# 첫째 줄에 수열 A의 크기 N (1 ≤ N ≤ 1,000)이 주어진다.

# 둘째 줄에는 수열 A를 이루고 있는 Ai가 주어진다. (1 ≤ Ai ≤ 1,000)


# if __name__ == '__main__':

#   n = int(input()); nums = list(map(int, input().split()))
#   dp = [1] * (n)

#   for i in range(n):
#     for j in range(i):
#       if nums[i] > nums[j]:
#         dp[i] = max(dp[i], dp[j] + 1)

#   print(max(dp))

## * Optimizing ##
def sol():
    N = int(input())
    nums = [*map(int,input().split())]
    stack = [nums[0]]

    for i in nums[1:]:
        if stack[-1] < i:
            stack.append(i)
        else:
            for j,v in enumerate(stack):
                if i <= v:
                    stack[j] = i
                    break
    return len(stack)

print(sol())