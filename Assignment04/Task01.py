#Task 1: Read a File and Handle Errors
#open("sample.txt","xt")
file = "sample.txt"

try:
    print("Reading file content:")
    with open(file, "r") as f:
        for i, line in enumerate(f, start=1):
            print(f"Line{i}: {line.strip()}")
except FileNotFoundError:
    print(f"Error: The file '{file}' was not found")

