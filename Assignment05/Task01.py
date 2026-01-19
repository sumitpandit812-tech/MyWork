#Dict of students Name & their Marks
student_marks = {"sumit":80,"sanket":90,"abhishek":70,"yashpal":60,"pratik":50,"priya":77,"supriya":86,"gaytri":75}

name = input("Enter student name: ").lower()#INPUT convert into lower case for if user input in upper case to avoid not found

if name in student_marks:
    print(f"{name}'s marks are: {student_marks[name]}")
else:
    print("Student not found")