#Task 2: Write and Append Data to a File

file = "output.txt"
#write to file overwrite
with open(file, "wt") as f:
    user_add = (input(f"Enter text to write to the  file: "))
    f.write(user_add + "\n")
    print("Data successfully written to output.txt file")
    print(""
          )
#mode 'a' used for append the  data again
with open(file, "at") as f:
    append_data = input("Enter additonal text to append: ")
    f.write(append_data + "\n")#for separate line by line we added \n
    print("Data successfully appended to output.txt file")
    print("Data succesfully appended.")
    print(""
          )
#mode'r' used to  read the file
with open(file, "r") as f:
    print(f"Final content of output.txt file:")
    print(f.read())
    for line in f:
        print(f.read.strip())
