my_students={}
i = 1

def add_student():

    student_name = input("Enter student name: ")
    lab1 = int(input("Enter lab 1: "))
    lab2 = int(input("Enter lab 2: "))
    lab3 = int(input("Enter lab 3: "))
    lab4 = int(input("Enter lab 4: "))
    lab5 = int(input("Enter lab 5: "))
    Total = lab1 + lab2 + lab3 + lab4 + lab5
    student_percentage = (Total / 50)*100  #(total/50)*100
    student_average = (Total)/5   #(total)/5


    my_students.update({"student"+str(i):{"name":student_name,"lab1": lab1, "lab2": lab2, "lab3" : lab3, "lab4": lab4, "lab5": lab5, "percentage":student_percentage,"average":student_average}})
    i = i + 1



def delete_student():
     delete_student = input("Enter student name to delete: ")
     if delete_student in my_students:
         del my_students[delete_student]
         print("student deleted")

     else:
         print("student not found")


print





