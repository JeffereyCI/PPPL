class CommandManager:
    def __init__(self):
        self.history = []
        self.redo_stack = []
        self.all_commands = []

    def execute_command(self, command):
        command.execute()
        self.history.append(command)
        self.all_commands.append(("Execute", command))
        self.redo_stack.clear()

    def undo(self):
        if self.history:
            command = self.history.pop()
            command.undo()
            self.redo_stack.append(command)
            self.all_commands.append(("Undo", command))
        else:
            print("No commands to undo.")
            
    def redo(self):
        if self.redo_stack:
            command = self.redo_stack.pop()
            command.execute()
            self.history.append(command)
            self.all_commands.append(("Redo", command))
        else:
            print("No commands to redo.")

    def show_history(self):
        if not self.all_commands:
            print("No history available.")
        else:
            print("Command History:")
            for i, (action, command) in enumerate(self.all_commands):
                print(f"{i + 1}: {action} {command.__class__.__name__}")
        print("\n")