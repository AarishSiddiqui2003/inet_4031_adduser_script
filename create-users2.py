#!/usr/bin/python3
import os
import re
import sys

def main():
    # Prompting the user to select whether dry-run or not before processing input.
    dry_run = input("Would you like to run the code in 'dry-run' mode? (Y/N): ").strip() == 'Y'

    # Open the input file explicitly
    with open('create-users.input', 'r') as infile:
        for line in infile:
                  # Check if the line is a comment.
            if re.match("^#", line):
                if dry_run:
                    print(f"Skipping comment: {line.strip()}")
                continue
            # Splitting the line into fields and check for 5 fields.
            fields = line.strip().split(':')
            if len(fields) != 5:
                if dry_run:
                    print(f"Error: Line does not have enough fields: {line.strip()}")
                continue
            # Getting user information from fields.
            username = fields[0]
            password = fields[1]
            gecos = "%s %s,,," % (fields[3], fields[2])
            groups = fields[4].split(',')
             # Commands for creating user and setting password.
            user_cmd = f"/usr/sbin/adduser --disabled-password --gecos '{gecos}' {username}"
            passwd_cmd = f"/bin/echo -ne '{password}\n{password}' | /usr/bin/sudo /usr/bin/passwd {username}"
        # Execute commands or show through dry run.
            if dry_run:
                print(f"Dry run: would execute '{user_cmd}'")
                print(f"Dry run: would execute '{passwd_cmd}'")
            else:
                os.system(user_cmd)
                os.system(passwd_cmd)
        # Handle group assignments real and dry run.
            for group in groups:
                if group != '-':
                    group_cmd = f"/usr/sbin/adduser {username} {group}"
                    if dry_run:
                        print(f"Dry run: would assign {username} to {group}")
                    else:
                        os.system(group_cmd)

if __name__ == '__main__':
    main()

