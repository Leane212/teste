class Calculator:
    def add(self, a, b):
        return a + b

class Printer:
    def print_message(self, message):
        print(message)

class Application:
    def __init__(self, calculator, printer):
        self.calculator = calculator
        self.printer = printer

    def run(self):
        result = self.calculator.add(2, 3)
        self.printer.print_message(f'The result is {result}')
