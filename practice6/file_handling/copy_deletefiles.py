import shutil
import os

shutil.copy("data.txt", "backup.txt")
print("File copied to backup.txt")

if os.path.exists("data.txt"):
    os.remove("data.txt")
    print("data.txt deleted")
else:
    print("File not found")