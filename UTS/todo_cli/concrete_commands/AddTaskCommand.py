from command.Command import Command

class AddTaskCommand(Command):
    def __init__(self, receiver, task):
        self.receiver = receiver
        self.task = task
        self.index = None
        self.removed_task = None

    def execute(self):
        self.receiver.add_task(self.task)
        self.index = len(self.receiver.task) - 1

    def undo(self):
        if self.index is not None:
            self.removed_task = self.receiver.remove_task(self.index)

    def redo(self):
        if self.removed_task is not None:
            self.receiver.add_task(self.removed_task)
            self.index = len(self.receiver.task) - 1
            self.removed_task = None
        else:
            self.execute()