#Created by chankruze
# Python program to find the factorial of a number provided by the user.

# Initial Value
num = 7

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

factorial = 1

# check if the number is negative, positive or zero
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of",num,"is",factorial)