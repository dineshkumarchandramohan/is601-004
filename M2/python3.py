a1 = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]
a2 = [-1, 1, -2, 2, 3, -3, -4, 5]
a3 = ["-0.01", "-0.0001", "-.15"]
a4 = ["-1", "2", "-3", "4", "-5", "5", "-6", "6", "-7", "7"]


def process_array(num, arr):
    print("\n UCID:-dc648 \n Processing Array({}): \n\n".format(num))
    print(arr)
    print("\nPositive Output:\n")
    for y in arr:
        if(int(y)>=0):
            print(y,end=" ")
    # TODO add new code here to print the desired result


print("Problem 3")
process_array(1, a1)
process_array(2, a2)
process_array(3, a3)
process_array(4, a4)
