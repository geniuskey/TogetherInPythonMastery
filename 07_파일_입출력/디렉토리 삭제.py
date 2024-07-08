import os

directory = 'example_dir'

if os.path.exists(directory):
    os.rmdir(directory)
    print(f"{directory} has been deleted.")
else:
    print(f"{directory} does not exist.")