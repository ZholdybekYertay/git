with open("data.txt", "w") as f:
    f.write("Hello\n")
    f.write("Python\n")


with open("data.txt", "a") as f:
    f.write("Appended line\n")

print("File written and appended successfully.")