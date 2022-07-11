amount =0 
prime=True
for num in range(100,201):
    for i in range(2,num):
        if num%i!=0:
            prime = False
            break
    if (prime):
        print(num)
        amount+=1
    prime = True
print(amount)