tasks= []
while True:
    print("/n -TO DO LIST -")
    print("1 - Add Task")
    print("3 - Remove Task")
    print("4 - Exit")

    choice = input ("enter your choice")

    if choice =="1":
       task = input("Enter task:")
       if task.strip() == "":
           print("Task cannot be empty!")
       else:
           tasks.append(task)
           print("task added!")
    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks yet.")
        else:
            print("\nYour Tasks:")
            for i in range(len(tasks)):
                print(i+1,"-", tasks[i])
    elif choice == "3":
            if len(tasks)== 0:
                print("No tasks to remove.")
            else:
                for i in range(len(tasks)):
                    print(i+1,"-",tasks[i])

            num = int(input("Enter task number:"))
            if 1 <= num <= len(tasks):
                removed = tasks.pop(num-1)
                print("Removed:",removed)
            else:
                print("Invalid number")
    elif choice == "4":
        print("Goodbye")
        break
    else:
        print("invalid choice")      