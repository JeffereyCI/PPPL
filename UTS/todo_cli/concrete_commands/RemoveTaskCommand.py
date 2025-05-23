from command.Command import Command

class RemoveTaskCommand(Command):
    def __init__(self, receiver, index):
        self.receiver = receiver
        self.index = index
        self.removed_task = None

    def execute(self):
        self.removed_task = self.receiver.remove_task(self.index)

    def undo(self):
        if self.removed_task is not None:
            self.receiver.task.insert(self.index, self.removed_task)

    def redo(self):
        self.execute()