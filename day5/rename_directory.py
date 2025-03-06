import os

def rename_files(directory, prefix):
   
    if not os.path.exists(directory):
        print("Directory does not exist.")
        return
    
    for filename in os.listdir(directory):
        old_path = os.path.join(directory, filename)
        if os.path.isfile(old_path):  # Ensure it's a file, not a directory
            new_filename = prefix + filename
            new_path = os.path.join(directory, new_filename)
            os.rename(old_path, new_path)
            print(f'Renamed: {filename} -> {new_filename}')

directory_path = "/c/path/to/your/directory"  # Change this to your target directory
prefix = "new_"
rename_files(directory_path, prefix)
