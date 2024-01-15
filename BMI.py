# 1st input: enter height in meters e.g: 1.65
height = float(input())
# 2nd input: enter weight in kilograms e.g: 72
weight = int(input())

BMI = int(weight/(height*height))
print("Your BMI value is ",+BMI)