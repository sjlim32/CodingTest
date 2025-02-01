m, n = map(int, input().split())
print(m//n)
print(m%n)

# OPTIMIZING
print(*divmod(*map(int,input().split())))