Height=int(input("enter your height in cm"))
Weight=int(input("enter your weight in kg"))
print("Height is :" ,Height)
print("Weight is :" ,Weight)

bmi_formula= (Weight/(Height*Height))/1000
BMI=bmi_formula
print(" Your BMI is :", BMI)

if(BMI <18.5):
   print("Your are underweight")
elif(BMI==18.5 or BMI<=24.5):
   print("Your are normal")
elif(BMI==25 or BMI<=29.9):
   print("Your are overweight")
elif(BMI== 30 or BMI<=34.5):
   print("Your are obese ")
else:
   print("Your are extremely")
   







