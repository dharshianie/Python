numbers = []
for i in list(range(1000,3001)):
    s = str(i)
    if (int(s)%2==0):
        print ("The number is even:",i)
        numbers.append(s)
    else:
        print ("The number is odd:",i)
        numbers.append(s)
    print (",".join(numbers))
    
