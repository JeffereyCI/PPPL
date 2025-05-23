from interface.strategy import OperationStrategy

class AddOperation(OperationStrategy):
    def execute(self, a: int, b: int):
        return a + b