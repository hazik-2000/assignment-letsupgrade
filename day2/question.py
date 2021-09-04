number=int(input("emter the number"))
Prime=True
for i in range (2,number):
    if number%i==0:
        Prime=False
        break
    
if Prime==True:
    print("prime number")    
else:
    print("number is non prime")          
