import os #inbuilt module of python

# Specify the directory
directory = "/"

# Get the contents of the directory
contents = os.listdir(directory)

# Print each item
for item in contents:
    print(item)
