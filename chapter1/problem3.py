import os

# Specify the directory path
path = '/'

# List all files and directories
with os.scandir(path) as entries:
    for entry in entries:
        print(entry.name)
