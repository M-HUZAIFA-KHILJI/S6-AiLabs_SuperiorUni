#MUHAMMAD HUZAIFA KHILJI
#f24-002
#LAB_1 Todo Items mini Project

todoList=[] #empty List to store items of list

def addTask(task):
    todoList.append(task)
    print(f"task '{task} is added.")


def viewTask():
    if not todoList:
        print("your task : todo list is blank/empty.")
    else:
        print("\n Your Todo list:")
        for i, task in enumerate(todoList):
            print(f"{i + 1}.{task}")
        print("-"*20)

print("My Dynamic TodoList")
while True:
        print("\nSelect listed option : ")
        print("1- Add")
        print("2- View Task") 
        print("3- Exit")   
        
        choice=input("enter your choice (1,2,or 3):") 
        
        if choice == '1':
            task_to_add = input("Enter the task you want to add: ")
            addTask(task_to_add)
        elif choice == '2':
            viewTask()
        elif choice == '3':
            print("Exiting To-Do List program. Goodbye!")
            break # Exit the while loop
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

             
                
        