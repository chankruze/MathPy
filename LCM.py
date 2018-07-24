# Created by chankruze
# Python Program to find the L.C.M. of two input number

# define a function
def lcm(x, y):
   """This function takes two
   integers and returns the L.C.M."""

   # choose the greater number
   if x > y:
       greater = x
   else:
       greater = y

   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1

   return lcm
# Initial Value
num_01 = 24
num_02 = 58

while True:
    try:
        # Note: Python 2.x users should use raw_input, the equivalent of 3.x's input
        input_01 = int(input("Enter first number: "))
        input_02 = int(input("Enter second number: "))
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
		
num_01 = input_01
num_02 = input_02

print()
print(">_The L.C.M. of" + str(num_01) + " and " + str(num_02) + " is " + str(lcm(num_01, num_02)))

