print("Calculate Cutting Lenght Of Circular String".center(70))
print()
print("Developed By Muhammad Hamza Javed")
print()
Diameter_Of_Column=float(input("Enter Diameter Of Column in mm : "))
Clear_Cover=float(input("Enter Value Of Clear Cover in mm : "))
Stirrups_Diameter=float(input("Enter Diameter Of Stirrups in mm : "))
#Finding Diameter Of Circle D = 2 * r
r=Diameter_Of_Column/2
print("R is : ",r.__round__(3),"mm")
print()
#Now Finding Cutting Lenght
R=r-Clear_Cover-(Stirrups_Diameter/2)
print("Stirrup Radius From Radius Is : ",R.__round__(3),"mm")