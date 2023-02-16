class User:
    def __init__(self, name, contact, email, age, gender, address):
        self.name = name
        self.contact = contact
        self.email = email
        self.age = age
        self.gender = gender
        self.address = address
    def display(self):
        print("Name: ", self.name)
        print("Contact: ", self.contact)
        print("Email: ", self.email)
        print("Age: ", self.age)
        print("Gender: ", self.gender)
        print("Address: ", self.address)
    
name = input("Enter your name: ")
contact = input("Enter your contact number: ")
email = input("Enter your email: ")
age = input("Enter your age: ")
gender = input("Enter your gender: ")
address = input("Enter your address: ")

data = User(name,contact,email,age,gender,address)
data.display()
