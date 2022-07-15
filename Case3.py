
kpctokth = 50
Vtokpc = 30
VtoSR = 40
ThtoPP=45
thtobtb=50

Thai = 300
veitnam = 200
kpht = 60
PP = 170
SR = 80
btb=70
demand = [,70,170,100]
list1=[]
while demand:
    mininum = demand[0]
    for i in demand:
        
        if mininum>i:
            mininum =i 
    list1.append(mininum)
    demand.remove(mininum)
print(list1)









