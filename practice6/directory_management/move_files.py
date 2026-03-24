import shutil
import os

with open("example.txt", "w") as f:
    f.write("Test file")

shutil.move("example.txt", "project/")
print("File moved to project/")

shutil.copy("project/example.txt", "example_copy.txt")
print("File copied back")