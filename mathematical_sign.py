class MathematicalSign:
    """class of generic math sign"""

    def __init__(self, sign: str, power: float, direction: str):
        """
        default is a plus sign
        :param sign: char represent the sign
        :param power: how powerful is the sign
        :param direction: right, left or middle
        """
        self._sign = sign
        self._power = power
        self._direction = direction

    def set_sign(self, sign: str):
        """
        :param sign: char represent the sign
        :return: void
        """
        self._sign = sign

    def set_power(self, power: int):
        """
        :param power: how powerful is the sign
        :return: void
        """
        try:
            power = int(power)
        except TypeError as err:
            print("must be a number")
            print(err)
        self._power = power

    def set_direction(self, direction: str):
        """
        :param direction: right, left or middle
        :return: void
        """
        self._direction = direction

    def get_sign(self) -> chr:
        """
        :return: the sign
        """
        return self._sign

    def get_power(self) -> float:
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
        if num2 == 0:
            raise ArithmeticError("Arithmetic Error: Divide By Zero")
        return round(num1 / num2, 10)


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
        if (num1 < 0 and -1 < num2 < 1) or (num1 == 0 and num2 < 0):
            raise ArithmeticError("Arithmetic Error: Complex Number")
        result = num1 ** num2
        if isinstance(result,complex):
            raise ArithmeticError("Arithmetic Error: Complex Number")
        return result


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
        return round((num1 + num2) / 2, 10)


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
        if num2 == 0:
            raise ArithmeticError("Arithmetic Error: Divide By Zero")
        return round(num1 % num2, 10)


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
        :return: Neg of operand
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
        if num1 < 0:
            raise ArithmeticError("Arithmetic Error: Can't factorized negative number")
        if num1 % 1 != 0:
            raise ArithmeticError("Arithmetic Error: Can't factorized floating number")
        num1 = int(num1)
        fac = 1
        for i in range(1, num1 + 1):
            fac *= i
        return fac


class HashTag(MathematicalSign):
    """ class of factorial sign, instance of math sign"""
    def __init__(self):
        """
        set parameters according to the attributions of HashTag
        """
        super().__init__('#', 6, 'right')

    @staticmethod
    def do_action(num1: float, num2: None) -> float:
        """
        :param num1: operand
        :param num2: None!!!!
        :return: HashTag of operand, can't hashtag negative numbers
        """
        if num1 < 0:
            raise ArithmeticError("Arithmetic Error: Can't HashTag negative number")
        num1 = str(num1)
        sum_of_digit = 0
        for digit in num1:
            if digit.isnumeric():
                digit = float(digit)
                sum_of_digit += digit
        return sum_of_digit


class UnaryMinus(MathematicalSign):
    """Strong Unary minus, occurs first every time, instance of math sign"""
    def __init__(self):
        """
        set parameters according to the attributions of Strong Unary Minus
        """
        super().__init__('_', 10, 'left')

    @staticmethod
    def do_action(num1: float, num2: float) -> float:
        """
        :param num1: operand
        :param num2: None!!!!
        :return: Neg of operand
        """
        return -1 * num1


class LesserUnaryMinus(MathematicalSign):
    """Weak Unary minus, occurs first every time, instance of math sign """
    def __init__(self):
        """
         set parameters according to the attributions of Weak Unary Minus
        """
        super().__init__(';', 3.5, 'left')

    @staticmethod
    def do_action(num1: float, num2: float) -> float:
        """
        :param num1: operand
        :param num2: None!!!!
        :return: Neg of operand
        """
        return -1 * num1


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
        case '_':
            return UnaryMinus()
        case ';':
            return LesserUnaryMinus()
    raise ValueError()


def is_operator(sign: str) -> bool:
    """
    :param sign: a string that represent the char in the expression
    :return: True if the char is an operator, False otherwise
    """
    if (sign == '+' or sign == '-' or sign == '*' or sign == '/' or sign == '^'
            or sign == '@' or sign == '$' or sign == '&' or sign == '%' or sign == '%' or sign == '~' or sign == '!'
            or sign == '#' or sign == '_' or sign == ';'):
        return True
    return False
