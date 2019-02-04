
num_float = []

def float_input():

    value_input = input("enter your number > ")

    float_value = float(value_input)

    print(f"you entered the float value {float_value}")

    num_float.append(float_value)

    print(num_float)
    num_float

    while len(num_float) < 10:
        print("enter another number")
        float_input()

    if len(num_float) == 10:
                print("just needed 10 values, no more :)")
    else:
        pass

def calculate_average(number_av):
    floataverage = sum(number_av) / len(number_av)
    print(f"the average of floating numbers you entered is {floataverage}")

float_input()

print(num_float)

calculate_average(num_float)
