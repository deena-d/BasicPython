fname = input("Enter file name: ") #test.txt
num_words = 0
with open(fname, 'r') as f:
 for line in f:
 words = line.split()
 num_words += len(words)
print("Number of words:")
print(num_words)

///Create another file:test.txt
hai
hello python
hai friends 