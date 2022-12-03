#print("Welcome: Create a new Patient")
#name = input("What is the patient's name? ")
#age = input("What is the patient's age? ")
#isNew = input("Is this a new patient? (True/False) ")

#correct = input("Name: " + name + "\nAge: " + age + "\nExisting Patient: " + isNew + "\nDoes this look correct? (True/False) ")

print("Welcome: Patient Registration System ")
name = input("Please enter the patient's name: ")
age = None
newPat = None

while(True):
    age_str = input("Please enter the patient's age: ")
    if age_str.isdigit():
        age = int(age_str)
        break
    else:
        print("Try entering an integer number.")

newPat = bool(input("Is this a new patient? (True/False) "))

#while(True):
    #newPat_str = input("Is this a new patient? ")
    #if bool(newPat_str):
        #newPat = bool(newPat_str)
        #break
    #else:
        #print("Try entering a boolean value.")