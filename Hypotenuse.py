import math
a,b=map(int,input().split())
h=a*a+b*b
hp=math.sqrt(h)
hyp='{:.2f}'.format(hp)
print(hyp)