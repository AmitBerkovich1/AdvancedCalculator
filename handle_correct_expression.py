import mathematical_sign


def calculate_unary(operands: list, operator: mathematical_sign.MathematicalSign) -> float:
    """
    :param operands: list of operands who needs to do action on
    :param operator: action
    :return: action on the operand
    """
    return operator.do_action(float(operands.pop()), None)


def calculate_binary(operands: list, operator: mathematical_sign.MathematicalSign) -> float:
    """
    :param operands: list of operands who needs to do action on
    :param operator: action
    :return: action on the operand
    """
    op1 = float(operands.pop())
    return operator.do_action(float(operands.pop()), op1)


def infix_to_postfix(infix: str) -> list:
    """
    :param infix: a valid math expression
    :return: list that represent the expression in postfix notation
    """
    stack = []
    postfix = []
    number = ''
    index = 0
    while index < len(infix):
        try:
            m = mathematical_sign.get_operator(infix[index])
        except ValueError:
            if infix[index] == '(':
                stack.append(infix[index])
                index += 1
            elif infix[index] == ')':
                while stack[-1] != '(':
                    postfix.append(stack.pop().get_sign())
                stack.pop()
                index += 1
            while index < len(infix) and (infix[index].isnumeric() or infix[index] == '.'):
                number += infix[index]
                index += 1
            if number != '':
                postfix.append(number)
            number = ''
        else:
            if not stack and '(' in stack and m.get_power() > stack[-1].get_power():
                stack.append(m)
            else:
                while stack and stack[-1] != '(' and stack[-1].get_power() >= m.get_power():
                    postfix.append(stack.pop().get_sign())
                stack.append(m)
            index += 1
    while stack:
        postfix += stack.pop().get_sign()
    return postfix


def calculate_postfix(postfix: list) -> float:
    """
    :param postfix: get a valid math expression in postfix notation
    :return: evaluation of the expression
    """
    stack = []
    index = 0
    while index < len(postfix):
        try:
            operator = mathematical_sign.get_operator(postfix[index])
        except ValueError:
            stack.append(postfix[index])
        else:
            if operator.get_direction() != 'middle':
                result = calculate_unary(stack, operator)
            else:
                result = calculate_binary(stack, operator)
            stack.append(result)
        index += 1
    return stack.pop()

