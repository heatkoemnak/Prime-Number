# Python Program to Check Whether the Binary Equivalent of a Given Number is Palindrome
 
# take input the number user
x=int(input('Enter a number: '))
 
# converting to binary
y=int(bin(x)[2:])
 
# reversing the binary 
out=str(y)[::-1] 
 
print("The binary representation of number:", y)
 
# checking the palindrome
if int(out)==y:
    print("The binary representation of the number is a palindrome.")
else:
    print("The binary representation of the number is not a palindrome.")