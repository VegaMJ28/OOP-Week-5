myEmployees = {}
i = 1

def add(i):
    name = input("Enter employee name: ")
    basic_pay = int(input("Enter basic pay: "))
    allowance = int(input("Enter allowance: "))
    deductions = int(input("Enter deductions: "))
    taxes = int(input("Enter taxes: "))
    gross_pay = basic_pay + allowance
    net_pay = gross_pay - deductions - taxes

    myEmployees.update({"employee"+ str(i): {"name": name, "basic pay": basic_pay, "allowance" : allowance, "deductions" : deductions, "taxes" : taxes, "gross pay": gross_pay, "net pay": net_pay}})

def delete():
    delete_employee = input("Enter employee key to be deleted: ")

    if delete_employee in myEmployees:
        del myEmployees[delete_employee]
        print("Employee deleted.")

    else:
        print("Employee not found.")

def modify():
    modify_employee = input("Enter employee key to be modified: ")

    if modify_employee in myEmployees:
        myEmployees[modify_employee]["basic pay"] = int(input("Enter basic pay: "))
        myEmployees[modify_employee]["allowance"] = int(input("Enter allowance: "))
        myEmployees[modify_employee]["deductions"] = int(input("Enter deductions: "))
        myEmployees[modify_employee]["taxes"] = int(input("Enter taxes: "))
        myEmployees[modify_employee]["gross pay"] = myEmployees[modify_employee]["basic pay"] +  myEmployees[modify_employee]["allowance"]
        myEmployees[modify_employee]["net pay"] =  myEmployees[modify_employee]["gross pay"] - myEmployees[modify_employee]["deductions"] - myEmployees[modify_employee]["taxes"]

    else:
        print("Employee not found.")



def display():
    if len(myEmployees) == 0:
        print("'myEmployees' is empty.")

    else:
        for employee in myEmployees:
            print(employee)
            print("name:", myEmployees[employee]["name"])
            print("basic pay:", myEmployees[employee]["basic pay"])
            print("allowance:", myEmployees[employee]["allowance"])
            print("deductions:", myEmployees[employee]["deductions"])
            print("taxes:", myEmployees[employee]["taxes"])
            print("gross pay:", myEmployees[employee]["gross pay"])
            print("net pay:", myEmployees[employee]["net pay"])

while 1:
    print("Employee Payroll Management")
    print("1. Add Employee")
    print("2. Delete Employee")
    print("3. Modify Employee")
    print("4. Display Employees")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 5:
        print("Exiting...")
        break

    elif choice == 1:
        add(i)
        i +=1

    elif choice == 2:
        delete()

    elif choice == 3:
        modify()

    elif choice == 4:
        display()

    else:
        print("Invalid choice.")
