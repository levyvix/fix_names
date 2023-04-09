import os
from glob import glob
import re

EXTENSION = "mkv"

# take all files in the current directory that ends with .mkv
all_files = glob("*")
files = glob(f"*.{EXTENSION}")
subs = glob("*.srt")

# loop through the files and rename them

for file in files:
    if "p" not in file:
        continue

    episode = re.search(r"\.(S\d+E\d+)", file).group(1)

    # rename the entire file with only the episode name
    new_name = f"{episode}.{EXTENSION}"

    # rename the file
    os.rename(file, new_name)


for sub in subs:
    os.remove(sub)

# remove every other file that is not a episode file
for file in all_files:
    if file not in files:
        os.remove(file)
