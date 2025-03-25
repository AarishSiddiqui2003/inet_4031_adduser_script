# INET4031 Add-User Script

## Program Description

This Python file provides an automated solution for system admins to add multiple users to a system. Usually this entails manually entering commands like `useradd` or `adduser`, setting passwords with `passwd`, and assigning groups with `gpasswd`. This script automates these processes by reading user data from a input file and executing the necessary system commands automatically.

## Program User Operation

After reading through this file you will be able to understand how user-processing.py functions. You will also be able to understand and create input files for the python function to create groups. Refer to the comments inside user-processing.py for detailed explanations on every function.

### Input File Format

The input file should be formatted as a colon-separated file where each line represents a user and contains the following:
- **Username**: The user's login name.
- **Password**: The password for the user.
- **Last Name**: User's last name.
- **First Name**: User's first name.
- **Groups**: Comma-separated list of groups the user belongs to. Use `-` if no groups.

EX: user04:pass04:Last04:First04:group01

To not process a line, start ite with a `#`. 

### Command Execution

To run the script, ensure that the Python file is executable. You may need to set this with the command:


chmod +x create-users.py

Then run with: ./create-user.py < create-user.input 

create-user.input can be replaced with any input file that is formatted correctly. 
