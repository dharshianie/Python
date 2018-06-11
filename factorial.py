num = int(input('enter number:' ))
fac = 1
for i in list(range (1, num + 1)):
    fac = fac * i

print("the value of", num, "factorial is", fac)

if (fac%2==0):
    print ("factorial is even number")
else:
    print ("factorial is odd number")
