## List all the files in list of folder that user provides

# 1) Read (Get)input from user (Folder)
# 2) For loop , folder --> List File
# 3) identifying Module (os Module = os.listdir)
# 4) Print file
# 5) Handle any known Error

import os

folders= input("Please provides List of folder with spaces in between :").split()

for folder in folders:
    
    try :
     files = os.listdir(folder)
    
    except FileNotFoundError:
      print("Please provide a valid folder name , looks like this folder doesn't exist" + folder)
      continue

    except PermissionError:
      print("no access to this folder : " , folder)
      continue

    print("=== Listing file From selected Folder " + folder)
   
    for file in files :
      print(file)
