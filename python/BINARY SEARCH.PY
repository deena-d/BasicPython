def binary_search(item_list,item):
 first = 0
 last = len(item_list)-1
 found = False
 while( first<=last and not found):
 mid = (first + last)//2
 if item_list[mid] == item :
 found = True
 print("Element found in the position:",mid)
 else:
 if item < item_list[mid]:
 last = mid - 1
 else:
 first = mid + 1
 if (found == False):
 print("Element not found")
a=[]
n=int(input("Enter the number of elements:"))
for i in range(0,n):
 b=int(input("Enter the element:"))
 a.append(b)
x=int(input("Enter the number to be searched:"))
binary_search(a,x)