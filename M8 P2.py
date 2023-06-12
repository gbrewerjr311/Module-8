#Greg Brewer
#6/4/23
#Problem Greater than 10, less than 10, or equal to 10

def check_sum():
    input1 = float(input("Enter the first input: "))
    input2 = float(input("Enter the second input: "))

    sum_of_inputs = input1 + input2

    if sum_of_inputs > 10:
        print("The sum is greater than 10.")
    elif sum_of_inputs < 10:
        print("The sum is less than 10.")
    else:
        print("The sum is equal to 10.")


check_sum()
