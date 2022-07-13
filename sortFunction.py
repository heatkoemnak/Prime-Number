#print list withot sort function and the element has the same index 
list = [0,-2,5,1,5,3,7,4,9,3,8,6,10]
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
answer is it will compare the first index of the element then remove that one
note : it remove the first occurence of the object .;

# # 9. Given an array arr[] of n elements, write a Python function to search a given element x in arr[].
# # arr=[1,2,3,4,5,5,6,78,9,10]

# arr = [1,2,3,4,5,6,7]
# # arr1=[]
# # n=2
# while 
# for n in arr:
#     if n in arr:
#         if n<=5:
#             print(n)
#         # print(n)


