import os


directory = 'example_dir'

if not os.path.exists(directory):
    os.makedirs(directory)
    print(f"{directory} has been created.")
else:
    print(f"{directory} already exists.")