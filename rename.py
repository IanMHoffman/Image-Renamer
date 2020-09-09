import os
from pathlib import Path
from datetime import datetime

# This is a short scrip that is used to take image files and convert them to a
# standard name using the date and time from the meta data
# Example: IMG_12345.jpg to 20200909_235959.jpg
# Just drag the file to the folder you want to rename and execute

# convert a uinix time stampt to a readable date time
def unix_date_conversion(unix_time):
    # If you want to chang ethe format simply chage the format below
    return datetime.utcfromtimestamp(unix_time).strftime('%Y%m%d_%H%M%S')

cwd = os.getcwd()

print("Currently renaming in folder: " + cwd)

count = 0

for path in Path(cwd).iterdir():
    if path.is_file():
        if path.suffix == '.jpg': # only continue if it is a jpeg image
            meta_data = path.stat()
            ctime = meta_data.st_ctime
            mtime = meta_data.st_mtime

            if mtime < ctime:
                date_created = unix_date_conversion(mtime)
            else:
                date_created = unix_date_conversion(ctime)

            new_filename = date_created + path.suffix #append extension
            print(f"Renaming: {path.name} To: {new_filename}")
            os.rename(path, new_filename)
            count += 1
print(f"Renamed a total of {count} images.")


