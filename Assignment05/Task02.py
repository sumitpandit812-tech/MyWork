#Task 2: Demonstrate List Slicing
#Create list

original = (list (range(1,11)))
print(f"Original list: {original}")

#extracting first five by using the index slicing
extracted = original[:5]
print(f"Extracted first five elements: {extracted}")

#for revesed negative indexing to start from end
reversed = extracted[::-1]
print(f"Reversed Extracted elements: {reversed}")
