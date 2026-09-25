myEmployees = {}
i = 1

def add(i):
    name =
    basic_pay =
    allowance =
    deductions =
    taxes =
    gross_pay =
    net_pay =

    myEmployees.update({"employee"+str(i): {"name": }})

def delete():
    delete_employee =

def modify():
    modify_employee =

    if modify_employee in myEmployees:
        myEmployees[modify_employee]["basic pay"]=


def display():
    if len(myEmployees) ==0:
        print("No employees found")

    else:
        for employee in myEmployees:
            print(employee)
            print("name:", myEmployees[employee]["name"])

