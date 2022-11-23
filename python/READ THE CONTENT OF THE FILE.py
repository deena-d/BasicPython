fname = input("Enter file name: ") #test.txt
with open(fname, 'r') as f:
 for line in f:
 print (line.upper())
 
 
 ///Create another file:test.txt

hai
hello python
hai friends