# Created by chankruze
# Python program to display all the prime numbers within an interval

print("Python program to display all the prime numbers within an interval")
print()

# change the values of lower and upper for a different result
lower = 900
upper = 1000

while True:
    try:
        # Note: Python 2.x users should use raw_input, the equivalent of 3.x's input
        input_num_01 = int(input("Enter the lower number of the interval : "))
        input_num_02 = int(input("Enter the upper number of the interval : "))
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
lower = input_num_01
upper = input_num_02

print("Prime numbers between",lower,"and",upper,"are:")

for num in range(lower,upper + 1):
   # prime numbers are greater than 1
   if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
           print(num)