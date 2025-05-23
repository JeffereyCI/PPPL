from context.calculator import Calculator
from concrete_strategy.add_operation import AddOperation
from concrete_strategy.subtract_operation import SubtractOperation
from concrete_strategy.multiply_operation import MultiplyOperation
from concrete_strategy.divide_operation import DivideOperation

def main():
    calculator = Calculator(AddOperation())
    result = None

    while True:            
        print("\n")
        choice = input("Opsi\n1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Clear\n6. exit\n Masukan pilihan : ")

        if choice == '6':
            break
        elif choice == '5':
            result = None
            print("perhitungan dibersihkan")
            print("\n")
            continue
        elif choice not in ['1', '2', '3', '4']:
            print("Input tidak valid")
            print("\n")
            continue

        if result is None:
            a = int(input("Masukan nilai pertama: "))
        else:
            a = result
            print(f"Nilai pertama: {a}")

        b = int(input("Masukan nilai kedua: "))

        if choice == '1':
            calculator.set_strategy(AddOperation())
        elif choice == '2':
            calculator.set_strategy(SubtractOperation())
        elif choice == '3':
            calculator.set_strategy(MultiplyOperation())
        elif choice == '4':
            calculator.set_strategy(DivideOperation())

        result = calculator.calculate(a, b)
        print(f"Hasil: {result:.2f}")
        print("\n")

if __name__ == "__main__":
    main()