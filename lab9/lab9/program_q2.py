# You are not allowed to modify all the codes in this file
import os
import os_command.directory

def main():
    list_directory = os_command.directory.get_directory_list(os.getcwd())
    list_file = os_command.directory.get_file_list(os.getcwd())
    
    print("List of directories in path", os.getcwd())
    for i in list_directory:
        print (i)
    print("List of files in path", os.getcwd())
    for i in list_file:
        print (i)

if __name__ == "__main__":
    main()
