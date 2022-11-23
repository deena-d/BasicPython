list1=[4,1,2,5,3]
search=int(input("Enter the Search Number:"))
found=False
for i in range(0,len(list1)):
 if search==list1[i]:
 print("%d Number is Found in the Position:%d" %(search,i))
 found=True
if found==False:
 print("%d Number is Not Found in the List" %(search)