#removing the file
import os
file_path = "hi.html"
if os.path.exists(file_path):
    print("file exists")
    os.remove(file_path)
    print("file removed")
else:
    print("file not exists")