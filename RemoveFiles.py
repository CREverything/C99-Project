import time
import shutil
import os
def get_file_or_folder_age(path):
    # getting ctime of the file/folder
    # time will be in seconds
    ctime = os.stat(path).st_ctime

    # returning the time
    return ctime
def main():

    # initializing the count
    deleted_folders_count = 0
    deleted_files_count = 0

    # specify the path
    path = input("Enter the directory:\n")

    # specify the days
    days = 30

    # converting days to seconds
    # time.time() returns current time in seconds
    seconds = time.time() - (days * 24 * 60 * 60)
    
    if(os.path.exists(path)):

        for root_folder, folders, files in os.walk(path):
            if(seconds>= get_file_or_folder_age(root_folder)):
                remove_folder(root_folder)
                deleted_folders_count += 1 # incrementing count

				# breaking after removing the root_folder
				break
            else:
                for folder in folders:
                    folder_path = os.path.join(root_folder, folder)
                
					# comparing with the days
					if seconds >= get_file_or_folder_age(folder_path):

						# invoking the remove_folder function
						remove_folder(folder_path)
						deleted_folders_count += 1 # incrementing count


                for file in files:

					# file path
					file_path = os.path.join(root_folder, file)

					# comparing the days
					if seconds >= get_file_or_folder_age(file_path):

						# invoking the remove_file function
						remove_file(file_path)
						deleted_files_count += 1 # incrementing count
    else:
        if seconds >= get_file_or_folder_age(path):

            # invoking the file
            remove_file(path)
            deleted_files_count += 1 # incrementing count