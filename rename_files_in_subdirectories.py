import os
import shutil


def rename_files_in_directory(root_directory):
    for subdir, dirs, files in os.walk(root_directory):
        if subdir != root_directory:
            # Sort files alphabetically (case insensitive)
            files.sort(key=lambda s: s.lower())

            counter = 1
            for file in files:
                old_filepath = os.path.join(subdir, file)
                new_filename = f"{os.path.basename(subdir)} {counter}"
                new_filepath = os.path.join(subdir, new_filename)

                # Check for the file extension, and add it to the new filename
                file_extension = os.path.splitext(file)[1]
                if file_extension:
                    new_filepath += file_extension

                # Rename the file
                shutil.move(old_filepath, new_filepath)
                counter += 1


if __name__ == "__main__":
    root_directory = os.getcwd()  # Current directory
    rename_files_in_directory(root_directory)