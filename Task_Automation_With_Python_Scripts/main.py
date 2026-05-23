import os
import shutil


source_folder = "Task_Automation_With_Python_Scripts/source_images"

destination_folder = "Task_Automation_With_Python_Scripts/organized_images"


if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# Count moved files
moved_files = 0

try:

    
    files = os.listdir(source_folder)

   
    for file in files:

       
        if file.endswith(".jpg"):

            # Create full file paths
            source_path = os.path.join(source_folder, file)

            destination_path = os.path.join(destination_folder, file)

            # Move file
            shutil.move(source_path, destination_path)

            # Increase counter
            moved_files += 1

            print(file, "moved successfully")

    print("\nTotal Files Moved:", moved_files)


except FileNotFoundError:
    print("Source folder not found.")


except Exception as error:
    print("Error:", error)