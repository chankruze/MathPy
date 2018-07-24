# Created BY Chankruze

# Initial Values
num_01 = 0
num_02 = 0
num_03 = 0

while True:
    try:
        # Note: Python 2.x users should use raw_input, the equivalent of 3.x's input
        input_01 = float(input("Enter first number : "))
        input_02 = float(input("Enter second number : "))
        input_03 = float(input("Enter third number : "))
    except ValueError:
        print("/////////////////////////////////////////////////////")
        print("//   Sorry, I did't understant that.               //")
        print("//   You must fill out a value to compare with !   //")
        print("/////////////////////////////////////////////////////")
        continue
    else:
        #input was successfully parsed!
        #we're ready to exit the loop.
        break

num_01 = input_01
num_02 = input_02
num_03 = input_03


if (num_01 > num_02) and (num_01 > num_03):
    i_am_largest = num_01

elif (num_02 > num_01) and (num_02 > num_03):
    i_am_largest = num_02

else:
    i_am_largest = num_03

print()
print(">_ The largest number between " + str(num_01) + " , " + str(num_01) + " and " + str(num_01) + " is " + str(i_am_largest))
