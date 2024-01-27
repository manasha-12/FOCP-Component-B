# Password Management System
This Python solution provides a set of command-line programs to manage a simplified password file. The password file contains entries with the format: username:real_name:encrypted_password.

# Programs Overview
## 1. adduser.py
Adds a new entry to the password file. The user is prompted to enter the desired username, real name, and password. If the username already exists, an error is displayed, and no change is made.
## 2. deluser.py
Removes an entry from the password file based on the username, which is known to be unique. If the user is not found, the program displays a message indicating that nothing was changed.
## 3. passwd.py
Changes a user's password. The user is prompted to enter their username, current password, and the new password twice. If the username is not found, the current password is invalid, or the passwords do not match, no change is made to the file.
## 4. login.py
Allows a user to enter a username and password, and the program reports whether or not they would be allowed to access the system. The password is not displayed as it is typed.

# Usage
To run the programs, execute the corresponding Python script in the command line. Provide the necessary inputs as prompted.

# File Structure
  * adduser.py: Adds a new user to the password file.
  * deluser.py: Deletes a user from the password file.
  * passwd.py: Changes a user's password.
  * login.py: Validates user credentials for login.
  * password_file.txt: Sample password file for testing.
  
Note: It is assumed that the password file (password_file.txt) exists and can be read. The file format is guaranteed to be as expected. All programs can be run individually without dependencies.
