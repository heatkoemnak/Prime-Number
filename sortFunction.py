#print list withot sort function
list = [0,-2,1,5,3,7,4,9,8,6,10]
list1=[]
#list2= 0

while list:
    mininum = list[0]
    for i in list:
        if mininum>i:
            mininum =i 
    list1.append(mininum)
    list.remove(mininum)
print(list1)