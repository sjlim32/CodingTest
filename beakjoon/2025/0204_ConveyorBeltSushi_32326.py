a = int(input())
b = int(input())
c = int(input())
print(a*3 + b*4 + c*5)

# OPTIMIZING
f=lambda:int(input())
print(3*f()+4*f()+5*f())

r,g,b=map(int,open(0))
print(r*3+g*4+b*5)

a,b=int,input;print(a(b())*3+a(b())*4+a(b())*5)