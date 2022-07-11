#How to count prime number
num = int(input("Enter two prime numbers:"))
amount=0

if num>0:
    for i in range(1,num+1):
     
        if (num%i)!=0: # check if i not eqaul to 0 it is prime number

            amount+=1
            
    print(amount)