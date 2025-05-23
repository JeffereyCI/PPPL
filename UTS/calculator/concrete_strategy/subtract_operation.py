from interface.strategy import OperationStrategy

class SubtractOperation(OperationStrategy):
    def execute(self, a: int, b: int):
        return a - b