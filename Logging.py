import os   #Imports OS module

user_dir = input('What directory would you like to save your file to? ')  # Gets input from user for directory

is_dir = os.path.isdir(user_dir)  # Validates that the directory exists

if is_dir == True:    # Informs the user if the directory exists or not
    print('Directory exists. Please continue')
else:
    print('Directory does not exist.  Goodbye.')  # I know, I was lazy here.
    quit()

user_file = input('Please enter the name of the file to save: ')  # Gets input from user for file name

user_name = input("What is your name? ").title()  # Gets user information
user_address = input("What is your street address? ")
user_phone = input("What is your phone number? (Entered XXX-XXX-XXXX) ")

file_path = user_dir + '\\' + user_file  # Sets variable for correct path

with open(file_path, 'a+') as file_object:  # Opens and closes file with users information
    file_object.write(user_name + ", " + user_address + ", " + user_phone + '\n')


with open(file_path, 'r') as f:  # Reads the last line entered to validate correct entry was saved
    lines = f.read().splitlines()
    last_line = lines[-1]
    print('You entered ' + last_line + ' into ' + user_file + '.')

