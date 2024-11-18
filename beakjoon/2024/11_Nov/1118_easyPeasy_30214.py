solver, total = map(int, input().split())
if total/2 <= solver:
  print("E")
else:
  print("H")

# OPTIMIZING
solver, total = map(int, input().split())
print("E" if solver>=total/2 else "H")