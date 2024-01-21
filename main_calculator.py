from input import check_input
from handle_correct_expression import infix_to_postfix, calculate_postfix


class Calculator(object):
    """class to represent the calculator"""
    def __init__(self, expression: str, result: float):
        """
        :param expression: math expression
        :param result: result of the expression
        """
        self._expression = expression
        self._result = result

    def set_expression(self, expression: str):
        """
        :param expression: input expression
        :return: void
        """
        self._expression = expression

    def set_result(self, result: float):
        """
        :param result: result of expression
        :return: void
        """
        self._result = result

    def get_expression(self) -> str:
        """
        :return: the expression
        """
        return self._expression

    def get_result(self) -> float:
        """
        :return: the result
        """
        return self._result


def main():
    calculate = Calculator(' ', 0)
    try:
        calculate.set_expression(check_input(input("Please Enter Your Expression\n")))
    except SyntaxError as err:
        print(err)
    except KeyboardInterrupt:
        print("Interrupted!")
    except EOFError as err:
        print(err)
    else:
        postfix = infix_to_postfix(calculate.get_expression())
        try:
            calculate.set_result(calculate_postfix(postfix))
        except ArithmeticError as err:
            print(err)
        else:
            print(calculate.get_result())


if __name__ == '__main__':
    main()
