import os

os.makedirs("project/data/files", exist_ok=True)
print("Directories created")

print("\nContents of current directory:")
print(os.listdir())

print("\nCurrent directory:")
print(os.getcwd())