def check(input):
    try:
       
        val = int(input)
        print("Input is an integer number. Number = ", val)
    except ValueError:
        try:
            
            val = float(input)
            print("Input is a float  number. Number = ", val)
        except ValueError:
            print("No.. input is not a number. It's a string")


input1 = input("Enter your Age ")
check(input1)

input2 = input("Enter any number ")
check(input2)

input2 = input("Enter the last number ")
check(input2)
