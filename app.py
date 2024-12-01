tasks = []

def printTasks():
    if len(tasks) != 0:
        for x in range(len(tasks)):
            print(str(x + 1) + ". " + tasks[x])

def operations():
    while True:
        print("\n1.Add (type 1 to add a new task) \n2.Delete(type 2 to delete a task task)\n3.Exit")
        userInput = int(input(""))

        if userInput == 1:
            task = input("Write your task: ")
            tasks.append(task)
            printTasks()

        elif userInput == 2:
            if len(tasks) == 0:
                print("There are no tasks. Add one first")
  
            rm = int(input("Type the ID of the task to delete: "))
            tasks.remove(tasks[rm - 1])
            printTasks()

        elif userInput == 3:
            break

        else:
            print("Please enter a valid number ")

print("Welcome to the To-Do App")
printTasks()
operations()