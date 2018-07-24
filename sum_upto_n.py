# Created by chankruze
# Python program to find the sum of natural numbers up to n where n is provided by user

# Initial Value
num = 25

while True:
    try:
        # Note: Python 2.x users should use raw_input, the equivalent of 3.x's input
        input_num = int(input("Enter a number: "))
    except ValueError:
        print("/////////////////////////////////////////////////////")
        print("//   Sorry, I did't understant that.               //")
        print("//   You must fill out a valid value to proceed !  //")
        print("/////////////////////////////////////////////////////")
        continue
    else:
        #input was successfully parsed!
        #we're ready to exit the loop.
        break

num = input_num

if num < 0:
   print("Enter a positive number")
else:
   sum = 0
   # use while loop to iterate un till zero
   while(num > 0):
       sum += num
       num -= 1
   print("The sum is",sum)