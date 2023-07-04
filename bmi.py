weight= input("enter the weight in kgs ")
height = input("enter the height in meters ")
bmi=int(weight)/float(height)**2
bmi_as_int=int(bmi)
print(bmi_as_int)

#for the height we need to mentioned as a float because
#2 is integer but height is an string this is what we mentioned "data type"
#height usually decimal number 
