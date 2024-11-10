import sys
print = sys.stdout.write

num = int(input())
for n in range(num, 0, -1):
  print(f"{' ' * (num - n)}{'*' * (2 * n - 1)}\n")