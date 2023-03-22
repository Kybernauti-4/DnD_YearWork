import os
import json

def storyHandler(folder):
    # Initialize an empty list to store the file paths
    file_paths = []

    # Walk through all the files and subfolders in the given folder
    for root, directories, files in os.walk(folder):
        # Iterate over the files in the current folder
        for filename in files:
            # Check if the file is named "storypart.txt"
            if filename == "storypart.json":
                if (os.path.dirname(os.path.join(root, filename))).split(os.path.sep)[-1].startswith('.'):
                    continue
                include = json.load(open(os.path.join(root, filename), 'r'))['include']
                if include:
                    # If it is and is to be included, add the full file path to the list
                    file_path = root
                    file_paths.append(file_path)

    # Return the list of file paths
    return file_paths

if __name__ == '__main__':
    # Get the list of all file paths in the directory tree at given path
    file_paths = storyHandler('story')
    # Print the list of file paths
    print(file_paths)