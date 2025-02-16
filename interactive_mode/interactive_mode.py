import datetime

name = input("Enter your name: ")

def get_age():
    while True:
        try:
            age = input("Enter your age: ")
            age = int(age)
            
            if age >= 0:
                return age
            else:
                 print("Please enter valid age")
        except:
            print("Invalid Input, Enter a valid age")

def approximate_birth_year(age):
    current_year = datetime.datetime.now().year
    approximate_birth_year = current_year - age
    return approximate_birth_year

age = get_age()
print(f"Your name is: {name}")
print(f"Approximate birth year: {approximate_birth_year(age)}")