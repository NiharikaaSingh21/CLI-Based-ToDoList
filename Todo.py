Tasks_File="tasks.txt"

#load tasks from the file if it doesnt contain any task return empty.
def load_tasks():
    
    item=[]
    try:
        with open (Tasks_File ,"r")as file:
            for line in file:
                item.append(line.strip())
    except FileNotFoundError:
        pass
    return item
#Save the tasks to the file.
def save_tasks(item):
    with open(Tasks_File,"w")as file:
        for task in item:
            file.write(task +"\n" )


#Display tasks.
def view_tasks(item):
     if not item:
        print("\n No tasks available.\n")
        return
     print("\nYour To-Do List")
     for idx, task in enumerate(item, 1):
          print(f"{idx}. {task}")
     print()

#Adding a task at a time.
def add_tasks(item):
    task=input("Enter new task").strip()
    if task:
        item.append(task)
        print("Task added")
    else:
        print("Cannot enter empty task")

def delete_tasks(item):
    view_tasks(item)

    if not item:
        return
    try:
        index=int(input("Enter the number of task to be removed "))
        if 1 <= index <= len(item):
            remove=item.pop(index-1)
            print(f"Removed task: {remove}\n")
        else:
            print("Task doesn't exist")
    except ValueError:
        print("Wrong Input!Please enter a valid number. ")

def main():
    item=load_tasks()

    while True:
        print("===== TO-DO LIST MENU =====")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Save Task")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == "1":
            view_tasks(item)
        elif choice =="2":
            add_tasks(item)
        elif choice =="3":
            delete_tasks(item)
        elif choice =="4":
            save_tasks(item)
            print("To-Do Updated !! Item Saved ")
        elif choice=="5":
            save_tasks(item)
            print("To-do Saved !! Now Exiting")
            break
    else:
        print("Invalid choice !! Enter a valid number ")

if __name__=="__main__":
    main()














