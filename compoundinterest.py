# program to find compound interest 
# p,r,t and A
# (Amount ) A = p*(1+ r/100)**t
# compound interest = A-p

p = float(input("enter the value of p: "))
r = float(input("enter the value of r: "))
t = float(input("enter the value of t: "))

A= p*(1+ r/100)**t

print("value of amount is:",round(A,2))

ci = A-p

print("compound interest is:",round(ci,2))