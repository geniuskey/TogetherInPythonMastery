import os
import glob

directory = '.'
pattern = '*.txt'

files = glob.glob(os.path.join(directory, pattern))
print(f"Text files in {directory}:")
for file in files:
    print(file)
