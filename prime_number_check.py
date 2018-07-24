# Created by chankruze
# Python program to check if the input number is prime or not

print("Python program to check if the input number is prime or not")
print()

# Initial Value
num = 407

# take input from the user

while True:
    try:
        # Note: Python 2.x users should use raw_input, the equivalent of 3.x's input
        input_num = int(input("Enter a number : "))
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

# prime numbers are greater than 1
if num > 1:
   # check for factors
   for i in range(2,num):
       if (num % i) == 0:
           print(num,"is not a prime number")
           print(i,"times",num//i,"is",num)
           break
   else:
       print()
       print(str(num) + " is a prime number")
       
# if input number is less than
# or equal to 1, it is not prime
else:
    print()
    print(str(num) + " is not a prime number")