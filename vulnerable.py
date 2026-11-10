filename = input("Enter filename: ")

# Opens the file without validating its path
try:
    with open(filename, "r") as file:
        print(file.read())
except Exception as e:
    print("Error:", e)
