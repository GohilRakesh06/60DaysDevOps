filename=input("Enter File Name : ")
f=open(filename)
num_words=0
with open(filename,'r') as f:
    for line in f:
        words=line.split()
        num_words+=len(words)
print(num_words)
     