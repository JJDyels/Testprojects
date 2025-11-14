# Random password generator
import random
import string

# Get place of use input from the user
place_of_use = input("Where will the password be used? ")

# Get username input from the user
username = input("Enter your username: ")

# Function to generate a random password
def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(characters) for i in range(length))
    return password

# Save the generated password to a file
open("password.txt", "a").write(str(place_of_use +" " + "Username: " + username + ", Password: " + generate_password()) + "\n")
print("username and password saved to file")