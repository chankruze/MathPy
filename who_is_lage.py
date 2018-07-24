num_01 = 12
num_02 = 34
num_03 = 40


if num_01 > num_02 :
    i_am_largest = num_01

    if num_01 > num_03:
        i_am_largest = num_01
    elif num_03 > num_01:
        i_am_largest = num_03
    else:
        i_am_largest = num_01


elif num_01 > num_03:
    i_am_largest = num_01

    if num_01 > num_02:
        i_am_largest = num_01
    elif num_02 > num_01:
        i_am_largest = num_02
    else:
        i_am_largest = num_01


elif num_02 > num_03:
    i_am_largest = num_02

    if num_02 > num_01:
        i_am_largest = num_02
    elif num_01 > num_02:
        i_am_largest = num_01
    else:
        i_am_largest = num_02


else:
    i_am_largest = num_03


print (i_am_largest)