from concrete_commands.AddTaskCommand import AddTaskCommand
from concrete_commands.RemoveTaskCommand import RemoveTaskCommand
from concrete_commands.MarkAsDoneCommand import MarkAsDoneCommand
from invoker.CommandManager import CommandManager
from receiver.TodoList import TodoList

def print_tasks(todo_list):
    print("=====================================\nCurrent tasks:")
    if todo_list.task is None:
        print("No tasks available.")
    else:
        for i, task in enumerate(todo_list.task):
            print(f"{i + 1}. {task}")
        print("\n")

def main():
    todo_list = TodoList()
    manager = CommandManager()

    while True:
        print('\n')
        print_tasks(todo_list)

        inputOption = input("Choose an option: \n1. Add Task\n2. Remove Task\n3. Mark as Done\n4. History\n5. Undo\n6. Redo\n7. Exit\nEnter Option : ")
        print('\n')
        if inputOption == "1":
            task = input("Enter task: ")
            command = AddTaskCommand(todo_list, task)
            manager.execute_command(command)
            print('\n')
        elif inputOption == "2":
            index = int(input("Enter task index to remove: ")) - 1
            command = RemoveTaskCommand(todo_list, index)
            manager.execute_command(command)
            print("\n")
        elif inputOption == "3":
            index = int(input("Enter task index to mark as done: ")) - 1
            command = MarkAsDoneCommand(todo_list, index)
            manager.execute_command(command)
            print("\n")
        elif inputOption == "4":
            manager.show_history()
            print("\n")
        elif inputOption == "5":
            manager.undo()
            print("\n")
        elif inputOption == "6":
            manager.redo()
            print("\n")
        elif inputOption == "7":
            break
        else:
            print("Invalid option. Please try again.\n")

if __name__ == "__main__":
    main()