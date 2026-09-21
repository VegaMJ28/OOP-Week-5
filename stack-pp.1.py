myqueue = []

def push():
    myqueue.append(int(input("Enter number to be added: ")))

def pop():
        myqueue.pop()


def display_queue():
    print(myqueue)

while 1:
    print("Your queue")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Display")
    print("4. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 4:
        break

    elif choice == 1:
        enqueue()

    elif choice == 2:
        dequeue()

    elif choice == 3:
        display_queue()

    else:
        print("Invalid choice")