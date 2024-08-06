import math
basic_salary=float(input())
hra=float(input())
da=float(input())
pf=(12/100)*basic_salary
gross_salary=basic_salary+hra+da+pf
print('{:.2f}'.format(pf))  
print('{:.2f}'.format(gross_salary))