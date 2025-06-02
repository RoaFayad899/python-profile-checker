#Ask user for informations
print("Please enter the following information:")
name = input("Your name in English: ")
age = float(input ("Your age:"))
gpa = float(input("Your GPA (between 0 and 5): "))
foi = input("Your field of interest: ")
graduation_status = input("Wethere you have graduated or not (just answer with yes or no): ")

#Checking some given information
if gpa<0 or gpa>5:
    gpa = float(input("Re-enter your GPA please, it must be between 0 and 5: "))
    
if graduation_status.lower() != "yes" and graduation_status.lower() != "no":
    graduation_status = input("Please answer wethere you have graduated or not with only yes or no: ")

#Setting eligibiliy conditions
scholarship_eligibility = age<25 and gpa>=3.5 and graduation_status=="yes"
internship_eligibility = age<30 and gpa>=2.5


