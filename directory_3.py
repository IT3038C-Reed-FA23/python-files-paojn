import os
import shutil

def create_directory_and_copy_files(source_dir, destination_dir):
    try:
        # Create the destination directory if it doesn't exist
        if not os.path.exists(destination_dir):
            os.makedirs(destination_dir)


        # List files in the source directory
        files_to_copy = os.listdir(source_dir)

        for file in files_to_copy:
            source_file = os.path.join(source_dir, file)
            destination_file = os.path.join(destination_dir, file)
            # copy the file
            shutil.copy(source_file, destination_file)

        print(f"Files copied from '{source_dir}' to '{destination_dir}'.")

    except Exception as e:
        print(f"An error occurred: {e}")
