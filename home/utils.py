from home.models import student
import time

def run_this_function():
    print('Function started')
    time.sleep(1)
    print('Function executed')

def creation_of_data():
    last_num = 3  # Define the number of iterations
    for _ in range(last_num):  # Correctly iterating using range
        # Get input from the user
        name = input("Enter the name: ")
        age = int(input("Enter the age: "))
        email = input("Enter the email: ")
        address = input("Enter the address: ")

        # Create a student object
        Student = student(
            name=name,
            age=age,
            email=email,
            address=address
        )

        # Save the object to the database
        Student.save()
        print("Student data saved successfully!")
