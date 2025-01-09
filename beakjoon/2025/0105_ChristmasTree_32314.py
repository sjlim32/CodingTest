tree = int(input())
watt, adapter = map(int, input().split())

if adapter * tree <= watt:
  print(1)
else:
   print(0)

# OPTIMIZING
print(1 if tree * adapter <= watt else 0)