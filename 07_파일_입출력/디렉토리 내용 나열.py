import os

directory = '.'

contents = os.listdir(directory)
print(f"Contents of {directory}:")
for item in contents:
    print(item)