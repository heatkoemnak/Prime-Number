num = int(input("Number:"))
temp = num
revers_num =0
while (num!=0):
    remind_num=num%10
    revers_num=(revers_num*10)+remind_num
    num = int(num//10)
print(revers_num)
if (revers_num==temp):
    print("True")
else:
    print("False")


