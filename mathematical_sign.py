class MathematicalSign:
    """class of generic math sign"""

    def __init__(self, sign: str, power: int, direction: str):
        """
        default is a plus sign
        :param sign: char represent the sign
        :param power: how powerful is the sign
        :param direction: right, left or middle
        """
        self._sign = '+'
        self._power = 1
        self._direction = 'm'
        self.set_sign(sign)
        self.set_power(power)
        self.set_direction(direction)

    def set_sign(self, sign: str):
        """
        :param sign: char represent the sign
        :return: void
        """
        try:
            sign = str(sign)
        except TypeError as err:
            print("Could not change sign")
            print(err)
        else:
            self._sign = sign

    def set_power(self, power: int):
        """
        :param power: how powerful is the sign
        :return: void
        """
        try:
            power = int(power)
        except TypeError as err:
            print("must be a whole number")
            print(err)
        if power < 1 or power > 6:
            raise ValueError()
        self._power = power

    def set_direction(self, direction: str):
        """
        :param direction: right, left or middle
        :return: void
        """
        try:
            direction = str(direction)
        except TypeError as err:
            print("must be a char")
            print(err)
        if direction != 'left' and direction != 'right' and direction != 'middle':
            print("direction must be: left, right or middle")
            raise ValueError()
        self._direction = direction

    def get_sign(self) -> chr:
        """
        :return: the sign
        """
        return self._sign

    def get_power(self) -> int:
        """
        :return: the power
        """
        return self._power

    def get_direction(self) -> chr:
        """
        :return: the direction
        """
        return self._direction

    def __str__(self) -> str:
        """
        :return: string representation of the sign
        """
        txt = ("sign = {sign} power = {power} direction = {direction}"
               .format(sign=self._sign, power=self._power, direction=self._direction))
        return txt

    @staticmethod
    def do_action(num1: float, num2: float) -> float:
        """
        :param num1: first operand
        :param num2: second operand
        :return: the action of the operator on the operand
        """
        return 0.0


class Plus(MathematicalSign):
    """class of Plus sign, instance of math sign"""

    def __init__(self):
        """
        set parameters according to the attributions of plus
        """
        super().__init__('+', 1, 'middle')

    @staticmethod
    def do_action(num1: float, num2: float) -> float:
        """
        :param num1: first operand
        :param num2: second operand
        :return: first operand plus second operand
        """
        return num1 + num2


class Minus(MathematicalSign):
    """class of Minus sign, instance of math sign"""

    def __init__(self):
        """
         set parameters according to the attributions of minus
        """
        super().__init__('-', 1, 'middle')

    @staticmethod
    def do_action(num1: float, num2: float) -> float:
        """
        :param num1: first operand
        :param num2: second operand
        :return: first operand minus second operand
        """
        return num1 - num2


class Mul(MathematicalSign):
    """class of mul sign, instance of math sign"""

    def __init__(self):
        """
         set parameters according to the attributions of multiplication
        """
        super().__init__('*', 2, 'middle')

    @staticmethod
    def do_action(num1: float, num2: float) -> float:
        """
        :param num1: first operand
        :param num2: second operand
        :return: first operand multiply by second operand
        """
        return num1 * num2


class Div(MathematicalSign):
    """ class of div sign, instance of math sign"""

    def __init__(self):
        """
        set parameters according to the attributions of multiplication
        """
        super().__init__('/', 2, 'middle')

    @staticmethod
    def do_action(num1: float, num2: float) -> float:
        """
        :param num1: first operand
        :param num2: second operand, must not be zero
        :return: first operand divide by second operand
        """
        try:
            return num1 / num2
        except ZeroDivisionError as err:
            print(err)


class Pow(MathematicalSign):
    """class of pow sign, instance of math sign"""

    def __init__(self):
        """
        set parameters according to the attributions of power
        """
        super().__init__('^', 3, 'middle')

    @staticmethod
    def do_action(num1: float, num2: float) -> float:
        """
        :param num1: first operand
        :param num2: second operand
        :return: first operand powered by second operand
        """
        try:
            return num1 ** num2
        except RuntimeError:
            print("can not power zero by zero")


class Avg(MathematicalSign):
    """ class of avg sign, instance of math sign"""

    def __init__(self):
        """
        set parameters according to the attributions of avg
        """
        super().__init__('@', 5, 'middle')

    @staticmethod
    def do_action(num1: float, num2: float) -> float:
        """
        :param num1: first operand
        :param num2: second operand
        :return: average of first and second operand
        """
        return (num1 + num2) / 2


class Max(MathematicalSign):
    """class of max sign, instance of math sign"""

    def __init__(self):
        """
         set parameters according to the attributions of max
        """
        super().__init__('$', 5, 'middle')

    @staticmethod
    def do_action(num1: float, num2: float) -> float:
        """
        :param num1: first operand
        :param num2: second operand
        :return: the max operand
        """
        if num1 > num2:
            return num1
        return num2


class Min(MathematicalSign):
    """class of min sign, instance of math sign"""

    def __init__(self):
        """
         set parameters according to the attributions of min
        """
        super().__init__('&', 5, 'middle')

    @staticmethod
    def do_action(num1: float, num2: float) -> float:
        """
        :param num1: first operand
        :param num2: second operand
        :return: the min operand
        """
        if num1 < num2:
            return num1
        return num2


class Modulo(MathematicalSign):
    """class of modulo sign, instance of math sign"""

    def __init__(self):
        """
        set parameters according to the attributions of modulo
        """
        super().__init__('%', 4, 'middle')

    @staticmethod
    def do_action(num1: float, num2: float) -> float:
        """
        :param num1: first operand
        :param num2: second operand
        :return: the rest of the division between the operands
        """
        try:
            return num1 % num2
        except ZeroDivisionError as err:
            print(err)


class Tilda(MathematicalSign):
    """class of tilda sign, instance of math sign """

    def __init__(self):
        """
        set parameters according to the attributions of tilda
        """
        super().__init__('~', 6, 'left')

    @staticmethod
    def do_action(num1: float, num2: None) -> float:
        """
        :param num1: operand
        :param num2: None!!!!
        :return: tilda of operand
        """
        return -1 * num1


class Factorial(MathematicalSign):
    """class of factorial sign, instance of math sign"""

    def __init__(self):
        """
        set parameters according to the attributions of factorial
        """
        super().__init__('!', 6, 'right')

    @staticmethod
    def do_action(num1: float, num2: None) -> float:
        """
        :param num1: operand
        :param num2: None!!!!
        :return: factorial of operand
        """
        fac = 1
        for i in range(1, num1 + 1):
            fac *= i
        return fac


class HashTag(MathematicalSign):
    def __init__(self):
        super().__init__('#', 6, 'right')

    @staticmethod
    def do_action(num1: float, num2: None) -> float:
        num1 = str(num1)
        sum_of_digit = 0
        for digit in num1:
            if digit.isnumeric():
                digit = float(digit)
                sum_of_digit += digit
        return sum_of_digit


def get_operator(sign: str) -> MathematicalSign:
    """
    :param sign: sign of operator
    :return: the object representation of the sign
    """
    match sign:
        case '+':
            return Plus()
        case '-':
            return Minus()
        case '*':
            return Mul()
        case '/':
            return Div()
        case '^':
            return Pow()
        case '@':
            return Avg()
        case '$':
            return Max()
        case '&':
            return Min()
        case '%':
            return Modulo()
        case '~':
            return Tilda()
        case '!':
            return Factorial()
        case '#':
            return HashTag()
    raise ValueError()


def is_operator(sign: str) -> bool:
    if (sign == '+' or sign == '-' or sign == '*' or sign == '/' or sign == '^'
            or sign == '@' or sign == '$' or sign == '&' or sign == '%' or sign == '%' or sign == '~' or sign == '!'
            or sign == '#'):
        return True
    return False
