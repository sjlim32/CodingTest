ans = ["Gnomes:"]
for _ in range(int(input())):
  r,g,b= map(int, input().split())
  ans.append("Ordered") if (r > g and g > b) or (r < g and g < b) else ans.append("Unordered")

print("\n".join(map(str, ans)))