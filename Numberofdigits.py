str = (input("enter the word:"))
l=0
d=0
for i in str:
    if i.isalpha():
        l+=1
    elif i.isdigit():
        d+=1
print ("number of letters:",l)
print ("number of digits:",d)
        
