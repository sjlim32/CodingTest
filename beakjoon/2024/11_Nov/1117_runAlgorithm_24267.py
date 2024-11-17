# 알고리즘 수행

# 리스트 A, 크기 n, 총합 sum
# i = 1부터 n-2까지 반복
# j = 2부터 n-1까지
# k = 3부터 n까지
# A[i] * A[j] * A[k]

# def MenOfPassion(n: int) :
#   if n < 3:
#     return print(4)

#   print(n * (n - 1) * (n - 2) // 6)
#   print(3)

# if __name__ == "__main__":
#   n = int(input())
#   MenOfPassion(n)

n = int(input())
print(n * (n - 1) * (n - 2) // 6)
print(3)