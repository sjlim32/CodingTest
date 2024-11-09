import sys
input = sys.stdin.readline
print = sys.stdout.write

n = int(input())
years = []

for _ in range(n):
  years.append(int(input()))

for j in range(n):
    print("Good\n") if (years[j] + 1) % (years[j] % 100) == 0 else print("Bye\n")


# OPTIMIZING

import sys
input = sys.stdin.readline
print = sys.stdout.write

for _ in range(int(input())):
    year = int(input())
    print("Good\n") if (year + 1) % (year % 100) == 0 else print("Bye\n")

# OPTIMIZING
N, *lis = map(int, open(0))
for l in lis:
    print(('Bye','Good')[(l+1)%(l%100)==0])