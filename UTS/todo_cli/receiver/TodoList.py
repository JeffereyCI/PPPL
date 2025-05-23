class TodoList:
    def __init__(self):
        self.task = []

    def add_task(self, task):
        self.task.append(task)
    
    def remove_task(self, index):
        if 0 <= index < len(self.task):
            return self.task.pop(index)
        else:
            raise IndexError("Task index out of range")
    
    def mark_as_done(self, index):
        if 0 <= index < len(self.task):
            self.task[index] = f"{self.task[index]} (done)"
        else:
            raise IndexError("Task index out of range")