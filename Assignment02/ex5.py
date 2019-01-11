name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print(f"Let's talk about {name}.")
print(f"He's {height} inches tall.")
print(f"He's {weight} pounds heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = age + height + weight

print(f"If I add {age}, {height}, and {weight} I get {total}.")

#enter value of inches to convert
inches = 10

#converting inches to cm
inches_to_cm = inches * 2.54

accurate_cm = round(inches_to_cm)

#printing the converted inches in cm

print(f"{inches} inches in cm is {inches_to_cm} cm")

print(f"{inches} inches in cm is {accurate_cm} cm, rounded off")
