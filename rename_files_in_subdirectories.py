"""
This script renames the files in each subdirectory of the current directory,
by prefixing the file names with the directory name followed by an incrementing number.
The files are sorted alphabetically (case insensitive) before renaming.

Usage:
1. Save this script as 'rename_files_in_subdirectories.py' in the root directory containing
   the subdirectories you want to process.
2. Open a terminal (or command prompt) and navigate to the root directory where the script is saved.
3. Run the script by entering the following command:
   python rename_files_in_subdirectories.py

Example:
Assuming you have the following directory structure:

root_directory/
├── 102/
│   ├── File1.txt
│   └── file2.txt
├── 103/
│   ├── another_file.txt
│   └── more_files.txt
└── rename_files_in_subdirectories.py

After running the script, the files will be renamed as follows:

root_directory/
├── 102/
│   ├── 102 1.txt
│   └── 102 2.txt
├── 103/
│   ├── 103 1.txt
│   └── 103 2.txt
└── rename_files_in_subdirectories.py
"""

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