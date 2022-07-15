num =int(input("Ennter Number:"))
# num=
# num=0
while (num!=0):
    remaind=num%10
    if (remaind!=0 and remaind!=1):
        print("This not binary number")
        break
    num =num//10
    if (num ==0):
        print("This is representation to binary number:")
    # print(remaind)
    
# if (num==1)