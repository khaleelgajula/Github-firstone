score=int(input("Enter the student's score (0-100):"))
if 90<=score<=100:
    print("Grade:A")
elif 80<=score<90:
    print("Grade:B")
elif 70<=score<80:
    print("Grade:c")
elif 60<=score<70:
    print("Grade:D")
elif 0<=score<60:
    print("Grade:F")
else:
    print("Invalid score")