from interface.strategy import OperationStrategy


class DivideOperation(OperationStrategy):
    def execute(self, a: int, b: int):
        return float(a / b)