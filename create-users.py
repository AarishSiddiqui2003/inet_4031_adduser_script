#!/usr/bin/python3

# INET4031
# Aarish Siddiqui
# 3/17/2025
# 3/25/2025

#os allows for interaction with the operating system through directory management and retrieval
#re is for regular expressions
#sys is for accessing variables used by interpretors such as command-line arguements
import os
import re
import sys

def main():
    for line in sys.stdin:

        #It is using regex to see if a string line starts with # and is done to identify comment lines.
        match = re.match("^#",line)

        #It uses strip() to remoe any whitespace and then split to divide the line at :
        fields = line.strip().split(':')

        #This if statement checks for is a line does not contain 5 fields
        #the loop continues if true
        #The if statement uses match to determine if a comment and then fields to check the structure and if either is false the line is skipped
        #It checks for 5 fields because it expects 5 to properly go through the data
        if match or len(fields) != 5:
            continue

        #The purpose of the next three lines is to extract the username, password, and full name
        username = fields[0]
        password = fields[1]
        gecos = "%s %s,,," % (fields[3],fields[2])

        #split is done to separate the group field from the inputted information
        groups = fields[4].split(',')

        #The print statements displays a password is being set for a new user
        print("==> Creating account for %s..." % (username))
        #cmd contains a command to send a password to passwd which creates the users password
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos,username)


        #print cmd
        #os.system(cmd)


        #indicates a password is being set for the user
        print("==> Setting the password for %s..." % (username))
        #Creates a command to set a password by echoing it and using sudo to put it into the passwd command
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password,password,username)

        #print cmd
        #os.system(cmd)

        for group in groups:
            #It ensures the group name is not hyphenated
            if group != '-':
                print("==> Assigning %s to the %s group..." % (username,group))
                cmd = "/usr/sbin/adduser %s %s" % (username,group)
                #print cmd
                #os.system(cmd)

if __name__ == '__main__':
    main()
