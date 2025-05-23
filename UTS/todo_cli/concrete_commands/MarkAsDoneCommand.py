from command.Command import Command

class MarkAsDoneCommand(Command):
    def __init__(self, receiver, index):
        self.receiver = receiver
        self.index = index
        self.prev_task = None

    def execute(self):
        if 0 <= self.index < len(self.receiver.task):
            self.prev_task = self.receiver.task[self.index]
            self.receiver.mark_as_done(self.index)

    def undo(self):
        if self.prev_task is not None and 0 <= self.index < len(self.receiver.task):
            self.receiver.task[self.index] = self.prev_task

    def redo(self):
        self.execute()