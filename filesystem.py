import os
import glob
import csv
root_dir = os.getenv('SystemRoot')

##starting function to prompt user which type of search they want
def file_search():
    user_input = input("Are you searching based on 1. Folder or 2. File: ")
    if user_input == "1":
        return folder_helper()
    elif user_input == "2":
        return file_helper()
    else:
        print("That is not a valid option, please try again")
        file_search()

##prompt user for which folder search they want
def folder_helper():
    user_input = input("Would you like to search based on string from 1. Start folder name or 2. End of folder name: ")
    if user_input == "1":
        return start_folder()
    elif user_input == "2":
        return end_folder()
    else:
        print("That is not a valid option, please try again")
        folder_helper()
    return

##prompt user for which file search they want
def file_helper():
    user_input = input("Would you like to search based 1. File names or 2. File extension: ")
    if user_input == "1":
        return file_name()
    elif user_input == "2":
        return file_extension()
    else:
        print("That is not a valid option, please try again")
        file_helper()
    return

##use glob and regexes to search from windows root to find desired files/folders
def start_folder():
    user_input = input("What starting string would you like to search for: ")
    user_input = "/" + user_input + "**/*"
    return glob.glob(root_dir + user_input, recursive=True)

def end_folder():
    user_input = input("What starting string would you like to search for: ")
    user_input = "/**" + user_input + "/*"
    return glob.glob(root_dir + user_input, recursive=True)

def file_name():
    user_input = input("What file name would you like to search for: ")
    user_input = "/**/*" + user_input + "*"
    return glob.glob(root_dir + user_input, recursive=True)

def file_extension():
    user_input = input("What file extension would you like to search for (don't include the dot): ")
    user_input = "/**/*." + user_input
    return glob.glob(root_dir + user_input, recursive=True)

##open csv file, grab necessary info from each file stored from functions above and write to csv
with open ("FileSearch.csv", "w", newline='') as f:
    write = csv.writer(f)
    fields = ["Folder Path","File Name","Creation Date","Modified Date","Date Accessed"]
    write.writerow(fields)
    for file in file_search():
        info = os.stat(file)
        path_and_file = file.split("\\")
        csv_info = ["\\".join(path_and_file[:-1]), path_and_file[-1], info.st_ctime, info.st_mtime, info.st_atime]
        write.writerow(csv_info)
    