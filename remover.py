## BEFORE START, MAKE SURE YOU HAVE INSTALLED rembg.
## https://pypi.org/project/rembg/

import os
from rembg import remove

# list to store files
dir_path = 'DIRECTORY OF THE FOLDER WITH YOUR PHOTOS'
list = []
for path in os.listdir(dir_path):
    # check if current path is a file
    if os.path.isfile(os.path.join(dir_path, path)):
        list.append(path)
print(list)

#for each photo, remove background
for photo in list:
    input_path= dir_path +photo
    output_path= 'DIRECTORY TO STORE PHOTOS WITH REMOVED BACKGROUND'+photo+'-removed.jpg'
    with open(input_path, 'rb') as i:
        with open(output_path, 'wb') as o:
            input = i.read()
            output = remove(input)
            o.write(output)
    
