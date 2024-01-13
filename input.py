from mathematical_sign import get_operator, is_operator
from handle_correct_expression import infix_to_postfix, calculate_postfix


def only_valid_sign(expression: str, index: int):
    """
    :param expression: Get an input expression
    :param index: Get the index of the char we want to check in the expression
    :return: Void if sign is valid, otherwise will raise Value Error
    """
    if (not expression[index].isnumeric() and expression[index] != '.' and expression[index] != '('
            and expression[index] != ')' and not is_operator(expression[index])):
        raise ValueError("Syntax Error: Invalid Char in Expression")


def not_empty_input(expression: str):
    """
    :param expression: Get an input expression
    :return: Void if input is not empty, otherwise will raise Value Error
    """
    if len(expression) == 0:
        raise ValueError("Syntax Error: Empty Input")


def check_binary_operator(expression: str, index: int):
    """
    :param expression: Get an input expression
    :param index: Get the index of the char we want to check in the expression
    :return: Void if operator is in a fine place, otherwise will raise Value Error
    """
    if index == 0 or index + 1 == len(expression):
        raise ValueError("Syntax Error: Binary Operator is Not in Valid Position")
    if not expression[index - 1].isnumeric() and expression[index - 1] != ')':
        raise ValueError("Syntax Error: Binary Operator is Not in Valid Position")
    if is_operator(expression[index + 1]):
        if get_operator(expression[index + 1]).get_direction() != 'left':
            raise ValueError("Syntax Error: Binary Operator is Not in Valid Position")
    if not expression[index + 1].isnumeric() and expression[index + 1] != '(':
        raise ValueError("Syntax Error: Binary Operator is Not in Valid Position")


def check_left_operator(expression: str, index: int):
    """
    :param expression: Get an input expression
    :param index: Get the index of the char we want to check in the expression
    :return: Void if operator is in a fine place, otherwise will raise Value Error
    """
    if index + 1 == len(expression):
        raise ValueError("Syntax Error: Left Unary Operator is Not in Valid Position")
    if not expression[index + 1].isnumeric() and expression[index + 1] != '(':
        raise ValueError("Syntax Error: Unary Operator is Not in Valid Position")


def check_right_operator(expression: str, index: int):
    """
    :param expression: Get an input expression
    :param index: Get the index of the char we want to check in the expression
    :return: Void if operator is in a fine place, otherwise will raise Value Error
    """
    if index == 0:
        raise ValueError("Syntax Error: Right Unary Operator is Not in Valid Position")
    if not expression[index - 1].isnumeric() and expression[index - 1] != ')':
        raise ValueError("Syntax Error: Right Unary Operator is Not in Valid Position")


def check_dot(expression: str, index: int) -> int:
    if index == 0 or index + 1 == len(expression):
        raise ValueError("Syntax Error: Dot is in invalid place")
    if not expression[index - 1].isnumeric():
        raise ValueError("Syntax Error: Dot is in invalid place")
    index += 1
    forward = 0
    while not is_operator(expression[index]) or index - 1 == len(expression):
        if not expression[index].isnumeric():
            raise ValueError("Syntax Error: Invalid float number, after the dot there are invalid characters")
        index += 1
        forward += 1
    return forward


def check_open_parenthesis(expression: str, index: int, curr_parenthesis: int) -> int:
    """
    :param expression: Get an input expression
    :param index: Get the place of the open parenthesis
    :param curr_parenthesis: the current count of parenthesis,open parenthesis raise the count by one
    :return: Raise value error if before and after the parenthesis there are invalid characters
            otherwise update the current count of parenthesis
    """
    if index + 1 == len(expression):
        raise ValueError("Syntax Error: Parenthesis is not in valid position")
    if is_operator(expression[index - 1]):
        if get_operator(expression[index - 1]).get_direction() == 'right':
            raise ValueError("Syntax Error: Missing operator before parenthesis")
    if is_operator(expression[index + 1]):
        if get_operator(expression[index + 1]).get_sign() != 'left':
            raise ValueError("Syntax Error: Missing operator before parenthesis")
    if not expression[index + 1].isnumeric():
        raise ValueError("Syntax Error: Missing operator before parenthesis")
    curr_parenthesis += 1
    return curr_parenthesis


def check_close_parenthesis(expression: str, index: int, curr_parenthesis: int) -> int:
    """
    :param expression: Get an input expression
    :param index: Get the place of the close parenthesis
    :param curr_parenthesis: the current count of parenthesis,close parenthesis decrease the count by one
    :return: Raise value error if before and after the parenthesis there are invalid characters
          or if curr parenthesis is negative, otherwise update the current count of parenthesis
    """
    if is_operator(expression[index - 1]):
        if get_operator(expression[index - 1]).get_direction() != 'right':
            raise ValueError("Syntax Error: Missing operator before parenthesis")
    if not expression[index - 1].isnumeric():
        raise ValueError("Syntax Error: Missing operator before parenthesis")
    if index + 1 != len(expression):
        if is_operator(expression[index + 1]):
            if get_operator(expression[index + 1]).get_direction() == 'left':
                raise ValueError("Syntax Error: Missing operator after parenthesis")
        if expression[index + 1].isnumeric():
            raise ValueError("Syntax Error: Missing operator after parenthesis")
    curr_parenthesis -= 1
    if curr_parenthesis < 0:
        raise ValueError("Syntax Error: You close parenthesis before opening them")
    return curr_parenthesis


def get_input() -> str:
    expression = input("Please Enter Your Expression\n")
    not_empty_input(expression)
    expression = expression.replace(" ", "")
    expression = expression.replace("\t", "")
    index = 0
    curr_parenthesis = 0
    while index < len(expression):
        mov = 1
        if not is_operator(expression[index]):
            if expression[index] == '(':
                curr_parenthesis = check_open_parenthesis(expression, index, curr_parenthesis)
            if expression[index] == ')':
                curr_parenthesis = check_close_parenthesis(expression, index, curr_parenthesis)
            if expression[index] == '.':
                mov = check_dot(expression, index)
            else:
                only_valid_sign(expression, index)
        else:
            operator = get_operator(expression[index])
            if operator.get_direction() == 'right':
                check_right_operator(expression, index)
            elif operator.get_direction() == 'left':
                check_left_operator(expression, index)
            elif operator.get_direction() == 'middle':
                check_binary_operator(expression, index)
        index += mov
    if curr_parenthesis != 0:
        raise ValueError("Syntax Error: Open parenthesis without closing them")
    if index == len(expression):
        return expression


def main():
    try:
        exprssion = get_input()
    except ValueError as err:
        print(err)
    else:
        lst = infix_to_postfix(exprssion)
        print(calculate_postfix(lst))


if __name__ == '__main__':
    main()
