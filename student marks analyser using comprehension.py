#student marks analyser using comprehension
#project we can upodate it in resume also


students = {
    "smith" : 67,
    "martin" :82,
    "scott" : 39,
    "allen" : 91,
    "miller" : 28,
    "virat" : 97
}
 
 #Dictonary comprehension for results(pass/fail)
result = {
    name : ("pass" if marks >40 else "fail")
    for name ,marks in students.items()
 }

#Dictionary comprehension for grades
grades = {
    name : (
        "A" if marks >=75 else
        "B" if marks >=60 else
        "C" if marks >=40 else
        "F"
    )
    for name , marks in students.items()
}

#List of passed students 
passed_students = [name for name,status in result.items() if status == "Pass"]


#List of failed students 
failed_students = [name for name,status in result.items() if status == "Fail"]

#Bonus list for toppers
toppers=[name for name , marks in students.items() if marks >=75]
print(f"result : {result}")
print(f"Grades : {grades}")
print(f"passed_students : {passed_students}")
print(f"failed_students : {failed_students}")
print(f"toppers(bonuslist) : {toppers}")