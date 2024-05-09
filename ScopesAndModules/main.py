# num = 1
#
# def foo():
#     num = 101
#
# foo()
# print(num)

# num = 1
#
# def foo():
#     num = num + 1
#
# if __name__ == '__main__':
#     foo()
#     print(num)

import mod


# if __name__ == '__main__':
#     print("Hello!")

num = 3
def is_name_defined_globally(name):
    global_namespace = globals()
    return name in global_namespace

if is_name_defined_globally('num'):
    print('my_variable is defined globally.')
else:
    print('my_variable is not defined globally.')


# import os
#
#
# def system_info():
#     # Get the operating system name
#     os_name = os.name
#
#     # Get the logged user
#     user_name = os.getlogin()
#
#     # Get the current working directory
#     cwd = os.getcwd()
#
#     return os_name, user_name, cwd
#
#
# if __name__ == "__main__":
#     os_name, user_name, cwd = system_info()
#     print("Operating System:", os_name)
#     print("Logged User:", user_name)
#     print("Current Working Directory:", cwd)

# import sys
#
#
# def reverse_print(args):
#     # Print command-line arguments in reverse order
#     for arg in reversed(args):
#         print(arg)
#
#
# if __name__ == "__main__":
#     # Get command-line arguments excluding the script name
#     args = sys.argv[1:]
#     reverse_print(args)

import os
import sys
import stat

def change_permissions(file_name):
    # Check if the file exists
    if not os.path.exists(file_name):
        print(f"File '{file_name}' does not exist.")
        return

    # Check if the file is executable
    if not os.access(file_name, os.X_OK):
        print(f"File '{file_name}' is not executable")
        # Get current file permissions
        file_stat = os.stat(file_name)
        # Set new permissions for owner and group
        new_permissions = file_stat.st_mode | stat.S_IXUSR | stat.S_IXGRP
        # Update file permissions
        os.chmod(file_name, new_permissions)
        print(f"Permissions of '{file_name}' changed successfully.")
    else:
        print(f"File '{file_name}' is already executable.")

if __name__ == "__main__":
    # Check if a file name is provided as a command-line argument
    if len(sys.argv) != 2:
        print("Usage: python script.py <file_name>")
        sys.exit(1)

    # Get the file name from the command-line argument
    file_name = sys.argv[1]
    # Call the function to change permissions
    change_permissions(file_name)
