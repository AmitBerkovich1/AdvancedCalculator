from mathematical_sign import get_operator, is_operator


def invalid_representation_of_minus(expression: str):
    """
    :param expression: Get an input expression
    :return: will raise syntax error for invalid chars that represent minus
    """
    if '_' in expression or ':' in expression:
        raise SyntaxError("Syntax Error: Invalid representation of minus")


def only_valid_sign(expression: str, index: int):
    """
    :param expression: Get an input expression
    :param index: Get the index of the char we want to check in the expression
    :return: Void if sign is valid, otherwise will raise Syntax Error
    """
    if (not expression[index].isnumeric() and expression[index] != '.' and expression[index] != '('
            and expression[index] != ')' and not is_operator(expression[index])):
        raise SyntaxError("Syntax Error: Invalid Char in Expression")


def not_empty_input(expression: str):
    """
    :param expression: Get an input expression
    :return: Void if input is not empty, otherwise will raise Syntax Error
    """
    if len(expression) == 0:
        raise SyntaxError("Syntax Error: Empty Input")


def reduce_minus(expression: str, index: int) -> tuple:
    """
    :param expression: Get an input expression
    :param index: Index of first minus
    :return: reduces the minuses according to even or odd number of minus is a row
    """
    count = 0
    origin = index
    while index < len(expression) and expression[index] == '-':
        check_left_minus(expression, index)
        count += 1
        index += 1
    if count % 2 == 0:
        return expression[:origin] + expression[origin + count:], 0
    else:
        return expression[:origin] + '_' + expression[origin + count:], 0


def check_left_minus(expression: str, index: int):
    """
    :param expression: Get an input expression
    :param index: the index of the minus we want to check
    :return: if the unary minus is in a valid position than vois, will raise a Syntax Error otherwise
    """
    if index + 1 == len(expression):
        raise SyntaxError("Syntax Error: Minus is not in valid place")
    if index != 0:
        if expression[index - 1] != '-' and expression[index - 1] != '(' and not is_operator(
                expression[index - 1]) and not expression[index - 1].isnumeric():
            raise SyntaxError("Syntax Error: Minus is not in valid place")
    if expression[index + 1] != '-' and not expression[index + 1].isnumeric() and expression[index + 1] != '(':
        raise SyntaxError("Syntax Error: Minus is not in valid place")


def check_weak_unary_minus(expression: str, index: int) -> bool:
    """
    :param expression: Get an input expression
    :param index:  the index of the minus we want to check
    :return: true if this is a unary minus with weak priority according to position, false otherwise
    """
    if index + 1 == len(expression):
        return False
    if index != 0:
        if is_operator(expression[index - 1]):
            if get_operator(expression[index - 1]).get_direction() == 'right':
                return False
            if expression[index + 1] != ')' and not expression[index + 1].isnumeric():
                return False
    if index == 0 or expression[index - 1] == '(':
        if is_operator(expression[index + 1]):
            if get_operator(expression[index + 1]).get_sign() != '-':
                return False
        if not expression[index + 1].isnumeric():
            return False
    if (expression[index + 1] == ')' or expression[index + 1].isnumeric()) and index != 0:
        return False
    return True


def minus_less_priority(expression: str, index: int) -> tuple:
    """
    :param expression: Get an input expression
    :param index: the index of the minus
    :return: same expression, replaced minus with representation of weak unary minus
    """
    return expression[:index] + ';' + expression[index + 1:], 1


def check_minus(expression: str, index: int) -> tuple:
    """
    :param expression: Get an input expression
    :param index: the index of the minus
    :return: replaces the minus according to his position, check if he is strong unary, weak unary or binary minus
    """
    if index != 0:
        if expression[index - 1] == '(' and expression[index + 1].isnumeric():
            return minus_less_priority(expression,index)
    try:
        check_binary_operator(expression, index)
    except SyntaxError:
        if check_weak_unary_minus(expression, index):
            return minus_less_priority(expression, index)
        else:
            check_left_minus(expression, index)
            return reduce_minus(expression, index)
    else:
        return expression, 1


def check_binary_operator(expression: str, index: int):
    """
    :param expression: Get an input expression
    :param index: Get the index of the char we want to check in the expression
    :return: Void if operator is in a fine place, otherwise will raise Syntax Error
    """
    if index == 0 or index + 1 == len(expression):
        raise SyntaxError("Syntax Error: Binary Operator is Not in Valid Position")
    if not expression[index - 1].isnumeric() and expression[index - 1] != ')':
        if is_operator(expression[index - 1]):
            if get_operator(expression[index - 1]).get_direction() != 'right':
                raise SyntaxError("Syntax Error: Binary Operator is Not in Valid Position")
        else:
            raise SyntaxError("Syntax Error: Binary Operator is Not in Valid Position")
    if not expression[index + 1].isnumeric() and expression[index + 1] != '(':
        if is_operator(expression[index + 1]):
            if get_operator(expression[index + 1]).get_direction() != 'left' and get_operator(
                    expression[index + 1]).get_sign() != '-':
                raise SyntaxError("Syntax Error: Binary Operator is Not in Valid Position")
        else:
            raise SyntaxError("Syntax Error: Binary Operator is Not in Valid Position")


def check_left_operator(expression: str, index: int):
    """
    :param expression: Get an input expression
    :param index: Get the index of the char we want to check in the expression
    :return: Void if operator is in a fine place, otherwise will raise Syntax Error
    """
    if index + 1 == len(expression):
        raise SyntaxError("Syntax Error: Left Unary Operator is Not in Valid Position")
    m = expression[index + 1]
    if (not expression[index + 1].isnumeric()) and expression[index + 1] != '(' and m != '-':
        raise SyntaxError("Syntax Error: Left Unary Operator is Not in Valid Position")


def check_right_operator(expression: str, index: int):
    """
    :param expression: Get an input expression
    :param index: Get the index of the char we want to check in the expression
    :return: Void if operator is in a fine place, otherwise will raise Syntax Error
    """
    if index == 0:
        raise SyntaxError("Syntax Error: Right Unary Operator is Not in Valid Position")
    if index + 1 != len(expression):
        if not is_operator(expression[index + 1]):
            if expression[index + 1] != ')':
                raise SyntaxError("Syntax Error: After Right Unary Operator must be a middle or right operator")
        else:
            if get_operator(expression[index + 1]).get_direction() == 'left':
                raise SyntaxError("Syntax Error: After Right Unary Operator must be a middle or right operator")
    if is_operator(expression[index - 1]):
        if get_operator(expression[index - 1]).get_direction() != 'right':
            raise SyntaxError("Syntax Error: Right Unary Operator is Not in Valid Position")
    elif not expression[index - 1].isnumeric() and expression[index - 1] != ')':
        raise SyntaxError("Syntax Error: Right Unary Operator is Not in Valid Position")


def check_dot(expression: str, index: int) -> int:
    """
    :param expression:  Get an input expression
    :param index: index: Get the index of the char we want to check in the expression
    :return: If operator is in a fine place return how much we need to move in order to get to the end of the float
    ,otherwise will raise Syntax Error
    """
    if index == 0 or index + 1 == len(expression):
        raise SyntaxError("Syntax Error: Dot is in invalid place")
    if not expression[index - 1].isnumeric() or not expression[index + 1].isnumeric():
        raise SyntaxError("Syntax Error: Dot is in invalid place")
    index += 1
    forward = 0
    while index < len(expression) and not is_operator(expression[index]) and expression[index] != ')':
        if not expression[index].isnumeric():
            raise SyntaxError("Syntax Error: Invalid float number, after the dot there are invalid characters")
        index += 1
        forward += 1
    return forward


def check_open_parenthesis(expression: str, index: int, curr_parenthesis: int) -> int:
    """
    :param expression: Get an input expression
    :param index: Get the place of the open parenthesis
    :param curr_parenthesis: the current count of parenthesis,open parenthesis raise the count by one
    :return: Raise Syntax Error if before and after the parenthesis there are invalid characters
            otherwise update the current count of parenthesis
    """
    if index + 1 == len(expression):
        raise SyntaxError("Syntax Error: Parenthesis is not in valid position")
    if index != 0:
        if expression[index-1].isnumeric():
            raise SyntaxError("Syntax Error: Missing operator before parenthesis")
        if is_operator(expression[index - 1]):
            if get_operator(expression[index - 1]).get_direction() == 'right':
                raise SyntaxError("Syntax Error: Missing operator before parenthesis")
    if is_operator(expression[index + 1]):
        if get_operator(expression[index + 1]).get_direction() != 'left' and get_operator(
                expression[index + 1]).get_sign() != '-':
            raise SyntaxError("Syntax Error: Missing operator before parenthesis")
    elif not expression[index + 1].isnumeric() and expression[index + 1] != '(':
        raise SyntaxError("Syntax Error: Missing operator before parenthesis")
    curr_parenthesis += 1
    return curr_parenthesis


def check_close_parenthesis(expression: str, index: int, curr_parenthesis: int) -> int:
    """
    :param expression: Get an input expression
    :param index: Get the place of the close parenthesis
    :param curr_parenthesis: the current count of parenthesis,close parenthesis decrease the count by one
    :return: Raise Syntax Error if before and after the parenthesis there are invalid characters
          or if curr parenthesis is negative, otherwise update the current count of parenthesis
    """
    if is_operator(expression[index - 1]):
        if get_operator(expression[index - 1]).get_direction() != 'right':
            raise SyntaxError("Syntax Error: Missing operator before parenthesis")
    elif index + 1 != len(expression):
        if is_operator(expression[index + 1]):
            if get_operator(expression[index + 1]).get_direction() == 'left':
                raise SyntaxError("Syntax Error: Missing operator after parenthesis")
        if expression[index + 1].isnumeric():
            raise SyntaxError("Syntax Error: Missing operator after parenthesis")
        if not is_operator(expression[index+1]) and expression[index+1] != ')':
            raise SyntaxError("Syntax Error: Missing operator after parenthesis")
    elif not expression[index - 1].isnumeric() and expression[index - 1] != ')':
        raise SyntaxError("Syntax Error: Missing operator before parenthesis")
    curr_parenthesis -= 1
    if curr_parenthesis < 0:
        raise SyntaxError("Syntax Error: You close parenthesis before opening them")
    return curr_parenthesis


def check_input(expression: str) -> str:
    """
    :param expression: Get an input expression
    :return: if all is valid, return a correct math expression, otherwise will raise a Syntax Error
    """
    invalid_representation_of_minus(expression)
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
            if operator.get_sign() == '-':
                tup = check_minus(expression, index)
                expression = tup[0]
                mov = tup[1]
            elif operator.get_direction() == 'right':
                check_right_operator(expression, index)
            elif operator.get_direction() == 'left':
                check_left_operator(expression, index)
            elif operator.get_direction() == 'middle':
                check_binary_operator(expression, index)
        index += mov
    if curr_parenthesis != 0:
        raise SyntaxError("Syntax Error: Open parenthesis without closing them")
    if index == len(expression):
        return expression
