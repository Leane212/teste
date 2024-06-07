from unittest.mock import Mock
from python.atividades.atividade15_application import Application, Calculator, Printer  

def test_application_run():
    calculator = Calculator()
    printer = Printer()
    printer.print_message = Mock()
    result = calculator.add(5, 5)

    app = Application(calculator, printer)
    app.run()

    result == 10
    printer.print_message.assert_called_once_with('The result is 5')