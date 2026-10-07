import json

def save_data():
    with open("Student_data.json","w") as f:
        json.dump(students,f,indent=4)

def load_data():
    try:
        with open("Student_data.json","r") as f:
            data=json.load(f)
            return data
    except (FileNotFoundError,json.JSONDecodeError): # handles error because of missing or invalid json file
        return []

students=load_data()

def get_marks(subject):
    while True:
        try:
            marks=int(input(f"enter marks of {subject}: "))

            if 0<=marks<=100:
                return marks
            else:
                print("marks should be between 0 and 100")
        except ValueError:
            print("please enter a valid number")

def add_student_data():
    name=input("Enter Students name: ").strip()
    if not name:
        print("Student name cannot be empty")
        return

    try:
        roll_no=int(input("Enter students roll no: "))
    except ValueError:
        print("Roll number must be a number")
        return

    if roll_no<=0:
        print("Roll number must be possitive")
        return

    for student in students:
        if student["roll_no"]==roll_no:
            print("this roll no already exists")
            return
        
    course=input("Enter students course: ").strip()

    if not course:
        print("course cannot be empty")
        return

    dbms_marks=get_marks("DBMS")
    python_marks=get_marks("Python")
    os_marks=get_marks("Operating System")
    cn_marks=get_marks("Computer Networks")
    maths_marks=get_marks("Maths")

    data={
        "name":name,
        "roll_no":roll_no,
        "course":course,
        "marks":{
            "dbms_marks":dbms_marks,
            "python_marks":python_marks,
            "os_marks":os_marks,
            "cn_marks":cn_marks,
            "maths_marks":maths_marks
        }
    }

    students.append(data)
    save_data()
    print("Student's Data Added Succesfully")

def view_student_data():
    if len(students)<=0:
        print("No Data Avaialable")
        return

    print("---------------------------------------------------------------")
    for student in students:
        print("Name= ",student["name"])
        print("Roll No= ",student["roll_no"])
        print("Course= ",student["course"])
        print("Marks: ")

        for subject,marks in student["marks"].items():
            print(subject,": ",marks)
        print("----------------------------------------------------------------")

def search_student_data():
    try:
        rn=int(input("Enter the roll no to fetch data : "))
    except ValueError:
        print("roll number must be a number")
        return 

    for student in students:
        if student["roll_no"]==rn:
            print(student["roll_no"],":")
            print("Name= ",student["name"])
            print("Course= ",student["course"])

            for sub,mark in student["marks"].items():
                print(sub,":",mark)

            return
            
    else:
            print("roll no ",rn,"not found")


def edit_student_data():
    try:
        rn=int(input("Enter the roll no to edit data: "))
    except ValueError:
        print("roll number must be a number")
        return

    for student in students:
        if student["roll_no"]==rn:
            name=input("Enter new name: ").strip()
            if not name:
                print("Students name cannot be empty")
                return

            course=input("Enter new Course: ").strip()
            if not course:
                print("Course cannot be empty")
                return

            student["name"]=name
            student["course"]=course

            student["marks"]["dbms_marks"]=get_marks("DBMS")
            student["marks"]["python_marks"]=get_marks("Python")
            student["marks"]["os_marks"]=get_marks("Operating System")
            student["marks"]["cn_marks"]=get_marks("Computer Networks")
            student["marks"]["maths_marks"]=get_marks("Maths")

            save_data()
            print("Students data uploaded succesfully")
            return
    else:
        print("Roll no not found")


def delete_student_data():
    try:
        rn=int(input("Enter the roll no to delete data: "))
    except ValueError:
        print("roll number must be a number")
        return
    
    for student in students:
        if student["roll_no"]==rn:
            students.remove(student)
            save_data()
            print("data removed successfully")
            return
    else:
        print("Roll no not found")

def view_result():
    try:
        rn=int(input("Enter roll no to view result: "))
    except ValueError:
        print("Roll number must be a integer")
        return

    for student in students:
        if student["roll_no"]==rn:
            total=sum(student["marks"].values())
            percentage=total/5

            if percentage >= 90:
                grade = "A+"
            elif percentage >= 80:
                grade = "A"
            elif percentage >= 70:
                grade = "B"
            elif percentage >= 60:
                grade = "C"
            elif percentage >= 50:
                grade = "D"
            else:
                grade = "F"

            if percentage>=40:
                result="PASS"
            else:
                result="FAIL"

            print("\n-------------------- Student Result --------------------")
            print("Name:", student["name"])
            print("Roll Number:", student["roll_no"])
            print("Course:", student["course"])

            print("\nMarks:")
            for subject, marks in student["marks"].items():
                print(subject, ":", marks)

            print("\nTotal Marks:", total, "/ 500")
            print("Percentage:", percentage, "%")
            print("Grade:", grade)
            print("Result:", result)
            print("---------------------------------------------------------")

            return
    else:
        print("Roll no",rn,"not found")
        

print("--------------------------Student Managment System-------------------------")
print("1.Add Student Data")
print("2.View Students")
print("3.Search Students")
print("4.Edit Students Data")
print("5.Delete Students Data")
print("6.View Result")
print("7.Exit")


while True:
    try:
        choice=int(input("Enter your choice: "))
    except ValueError:
        print("Please enter a valid number: ")
        continue

    match choice:
        case 1:
            add_student_data()
        case 2:
            view_student_data()
        case 3:
            search_student_data()
        case 4:
            edit_student_data()
        case 5:
            delete_student_data()
        case 6:
            view_result()
        case 7:
            print("Thankyou for using student managment system!!!")
            break
        case _:
            print("Invalid choice!!")