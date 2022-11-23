f=0
f1=0
f2=1
n=int(input("Enter the Range:"))
print(f1,f2,end=" ")
f=f1+f2
while f<n:
 f=f1+f2
 f1=f2
 f2=f
 print(f,end=" ")