import math
a,b=map(int,input().split())
l=a-b
lp=(l/a)*100
ans='{:.2f}'.format(lp)
print(ans)