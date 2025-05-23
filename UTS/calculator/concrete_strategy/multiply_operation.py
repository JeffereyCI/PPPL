from interface.strategy import OperationStrategy

class MultiplyOperation(OperationStrategy):
    def execute(self, a: int, b: int):
        return a * b