import os

old_name = 'old_example.txt'
new_name = 'new_example.txt'

if os.path.exists(old_name):
    os.rename(old_name, new_name)
    print(f"{old_name} has been renamed to {new_name}.")
else:
    print(f"{old_name} does not exist.")
