import os

def storyHandler(folder):
    # Initialize an empty list to store the file paths
    file_paths = []

    # Walk through all the files and subfolders in the given folder
    for root, directories, files in os.walk(folder):
        # Iterate over the files in the current folder
        for filename in files:
            # Check if the file is named "storypart.txt"
            if filename == "storypart.json":
                # If it is, add the full file path to the list
                file_path = root
                file_paths.append(file_path)

    # Return the list of file paths
    return file_paths