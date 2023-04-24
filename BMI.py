height = float(input("Whats your height:"))
weight = float(input("Whats your weight:"))

print("Height = " + str(height))
print("Weight = " + str(weight))
bmi = weight/height**2
print(bmi)
if bmi < 18.5:
    print("Underweight")
elif bmi <= 25.0 and bmi >= 18.5:
    print("Normal Weight")
else:
    print("Overweight")

