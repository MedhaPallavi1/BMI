weight = float(input("enter weight in kg"))
height = float(input("enter height in m"))
bmi = (weight)/(height**2)
print(bmi)
if bmi > 28:
    print("obese")
elif bmi > 25:
    print("overweight")
elif bmi > 18:
    print("normal BMI")
else:
    print("underweight")
    
