import sys
input = sys.stdin.readline
print = sys.stdout.write

M = int(input().rstrip())
S = set()

for _ in range(M):
  n = input().rstrip()

  if 'all' in n:
    S = set(range(1, 21))
  elif 'empty' in n:
    S = set()
  else:
    order, number = n.split()
    num = int(number)
    
    if order == 'add':
      S.add(num)
    elif order == 'remove':
      S.discard(num)
    elif order == 'toggle':
      if num in S:
        S.discard(num)
      else:
        S.add(num)
    elif order == 'check':
      if num in S:
        print("1\n")
      else:
        print("0\n")

# OPTIMIZING
import sys

read = sys.stdin.readline
write = sys.stdout.write

x = [False] * 21

m = int(read())
for _ in range(m):
    command = read().split()
    num = 0
    if len(command) > 1:
        num = int(command[1])
    if command[0] == 'add':
        x[num] = True
    elif command[0] == 'remove':
        x[num] = False
    elif command[0] == 'check':
        write(str(1 if x[num] else 0) + '\n')
    elif command[0] == 'toggle':
        x[num] = not x[num]
    elif command[0] == 'all':
        x = [True] * 21
    elif command[0] == 'empty':
        x = [False] * 21

# OPTIMIZING - 비트마스킹
import sys

input = sys.stdin.readline
write = sys.stdout.write

def main():
    n = int(input().strip())
    li = 0  # 비트마스크 활용
    
    for _ in range(n):
        line = input().split()
        op = line[0]
        
        if op == 'add':
            x = int(line[1])
            li |= (1 << (x - 1))
        elif op == 'check':
            x = int(line[1])
            write('1\n' if (li & (1 << (x - 1))) else '0\n')
        elif op == 'remove':
            x = int(line[1])
            li &= ~(1 << (x - 1))
        elif op == 'toggle':
            x = int(line[1])
            li ^= (1 << (x - 1))
        elif op == 'all':
            li = (1 << 20) - 1  # 20비트가 모두 1인 상태
        elif op == 'empty':
            li = 0

if __name__ == "__main__":
    main()