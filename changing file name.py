import os

# Set the path to your images directory
path = 'city_val'

# Get a list of all files in the directory
files = os.listdir(path)

# Sort the files based on their current names
files.sort()

# Set a starting index for the new sequence
new_index = 501

# Iterate through the files and rename them
for file in files:
    # Construct the new name using the new index
    new_name = f"{new_index}.jpg"  # Change the extension if your images have a different format

    # Create the full path for both the old and new names
    old_path = os.path.join(path, file)
    new_path = os.path.join(path, new_name)

    # Rename the file
    os.rename(old_path, new_path)

    # Increment the index for the next iteration
    new_index += 1
