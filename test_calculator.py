from main_calculator import calculate_postfix, infix_to_postfix, Calculator, check_input
import pytest


def test_simple_expression_addition():
    cal = Calculator('41+1', 0)
    cal.set_expression(check_input(cal.get_expression()))
    postfix = infix_to_postfix(cal.get_expression())
    result = calculate_postfix(postfix)
    assert result == 42


def test_simple_right_unary():
    cal = Calculator('3!+2', 0)
    cal.set_expression(check_input(cal.get_expression()))
    postfix = infix_to_postfix(cal.get_expression())
    result = calculate_postfix(postfix)
    assert result == 8


def test_simple_left_unary():
    cal = Calculator('~-3', 0)
    cal.set_expression(check_input(cal.get_expression()))
    postfix = infix_to_postfix(cal.get_expression())
    result = calculate_postfix(postfix)
    assert result == 3


def test_simple_failure_unary_operator():
    cal = Calculator('-~3', 0)
    with pytest.raises(SyntaxError):
        cal.set_expression(check_input(cal.get_expression()))


def test_simple_failure_binary_operator():
    cal = Calculator('3+^2', 0)
    with pytest.raises(SyntaxError):
        cal.set_expression(check_input(cal.get_expression()))


def test_white_spaces():
    cal = Calculator('   3    @     5', 0)
    cal.set_expression(check_input(cal.get_expression()))
    postfix = infix_to_postfix(cal.get_expression())
    result = calculate_postfix(postfix)
    assert result == 4


def test_simple_empty_input():
    cal = Calculator('', 0)
    with pytest.raises(SyntaxError):
        cal.set_expression(check_input(cal.get_expression()))


def test_simple_jibrish():
    cal = Calculator('2+sdc+2+dsjjsk', 0)
    with pytest.raises(SyntaxError):
        cal.set_expression(check_input(cal.get_expression()))


def test_simple_factorized_negative():
    cal = Calculator('4--3!', 0)
    cal.set_expression(check_input(cal.get_expression()))
    postfix = infix_to_postfix(cal.get_expression())
    with pytest.raises(ArithmeticError):
        calculate_postfix(postfix)


def test_invalid_sign():
    cal = Calculator('2_1', 0)
    with pytest.raises(SyntaxError):
        cal.set_expression(check_input(cal.get_expression()))


def test_invalid_dot():
    cal = Calculator('2.*3.', 0)
    with pytest.raises(SyntaxError):
        cal.set_expression(check_input(cal.get_expression()))


def test_complex_number():
    cal = Calculator('(3-5)^-0.5', 0)
    cal.set_expression(check_input(cal.get_expression()))
    postfix = infix_to_postfix(cal.get_expression())
    with pytest.raises(ArithmeticError):
        calculate_postfix(postfix)


def test_mul():
    cal = Calculator('2*5+7', 0)
    cal.set_expression(check_input(cal.get_expression()))
    postfix = infix_to_postfix(cal.get_expression())
    result = calculate_postfix(postfix)
    assert result == 17


def test_div():
    cal = Calculator('2/10/2', 0)
    cal.set_expression(check_input(cal.get_expression()))
    postfix = infix_to_postfix(cal.get_expression())
    result = calculate_postfix(postfix)
    assert result == 0.1


def test_zero_division():
    cal = Calculator('5/(3-3)', 0)
    cal.set_expression(check_input(cal.get_expression()))
    postfix = infix_to_postfix(cal.get_expression())
    with pytest.raises(ArithmeticError):
        calculate_postfix(postfix)


def test_power():
    cal = Calculator('2^2^3', 0)
    cal.set_expression(check_input(cal.get_expression()))
    postfix = infix_to_postfix(cal.get_expression())
    result = calculate_postfix(postfix)
    assert result == 64


def test_avg():
    cal = Calculator('2@2@1', 0)
    cal.set_expression(check_input(cal.get_expression()))
    postfix = infix_to_postfix(cal.get_expression())
    result = calculate_postfix(postfix)
    assert result == 1.5


def test_max():
    cal = Calculator('(2+1)$1', 0)
    cal.set_expression(check_input(cal.get_expression()))
    postfix = infix_to_postfix(cal.get_expression())
    result = calculate_postfix(postfix)
    assert result == 3


def test_min():
    cal = Calculator('(2+1)&1', 0)
    cal.set_expression(check_input(cal.get_expression()))
    postfix = infix_to_postfix(cal.get_expression())
    result = calculate_postfix(postfix)
    assert result == 1


def test_modulo():
    cal = Calculator('5%(6%3)', 0)
    cal.set_expression(check_input(cal.get_expression()))
    postfix = infix_to_postfix(cal.get_expression())
    with pytest.raises(ArithmeticError):
        calculate_postfix(postfix)


def test_factorial():
    cal = Calculator('3!!', 0)
    cal.set_expression(check_input(cal.get_expression()))
    postfix = infix_to_postfix(cal.get_expression())
    result = calculate_postfix(postfix)
    assert result == 720


def test_hashtag():
    cal = Calculator('99##', 0)
    cal.set_expression(check_input(cal.get_expression()))
    postfix = infix_to_postfix(cal.get_expression())
    result = calculate_postfix(postfix)
    assert result == 9


def test_complicated():
    cal = Calculator('(13-11)^(2!)+13*2*3', 0)
    cal.set_expression(check_input(cal.get_expression()))
    postfix = infix_to_postfix(cal.get_expression())
    result = calculate_postfix(postfix)
    assert result == 82


def test_complicated2():
    cal = Calculator('((--(--(5))+2)^2)#+4', 0)
    cal.set_expression(check_input(cal.get_expression()))
    postfix = infix_to_postfix(cal.get_expression())
    result = calculate_postfix(postfix)
    assert result == 17


def test_complicated3():
    cal = Calculator('(--(--(5))+2)^2)#+4*13', 0)
    with pytest.raises(SyntaxError):
        cal.set_expression(check_input(cal.get_expression()))


def test_complicated4():
    cal = Calculator('(((4.2%4)+0.8)^8.5+9)^2', 0)
    cal.set_expression(check_input(cal.get_expression()))
    postfix = infix_to_postfix(cal.get_expression())
    result = calculate_postfix(postfix)
    assert result == 100


def test_complicated5():
    cal = Calculator('(((0.5^2)+0.75)*30)#!-3', 0)
    cal.set_expression(check_input(cal.get_expression()))
    postfix = infix_to_postfix(cal.get_expression())
    result = calculate_postfix(postfix)
    assert result == 3


def test_complicated6():
    cal = Calculator('((-((0.5^2)+0.75)*30)#!)!', 0)
    cal.set_expression(check_input(cal.get_expression()))
    postfix = infix_to_postfix(cal.get_expression())
    with pytest.raises(ArithmeticError):
        calculate_postfix(postfix)


def test_complicated7():
    cal = Calculator('((3.5+~-3.5)$10)^(3@5)*(1.23#)', 0)
    cal.set_expression(check_input(cal.get_expression()))
    postfix = infix_to_postfix(cal.get_expression())
    result = calculate_postfix(postfix)
    assert result == 60000


def test_complicated8():
    cal = Calculator('(((3.5+~-3.5)&10)!+(1.23#))/(7!+(5@7))', 0)
    cal.set_expression(check_input(cal.get_expression()))
    postfix = infix_to_postfix(cal.get_expression())
    result = calculate_postfix(postfix)
    assert result == 1


def test_complicated9():
    cal = Calculator('((((3.2+4.8)%2)+8)^2)#*5', 0)
    cal.set_expression(check_input(cal.get_expression()))
    postfix = infix_to_postfix(cal.get_expression())
    result = calculate_postfix(postfix)
    assert result == 50


def test_complicated10():
    cal = Calculator('-((((3.2+4.8)%2)+8)^2)#*5', 0)
    cal.set_expression(check_input(cal.get_expression()))
    postfix = infix_to_postfix(cal.get_expression())
    with pytest.raises(ArithmeticError):
        calculate_postfix(postfix)


def test_complicated11():
    cal = Calculator('((~(2---3!)^0.5)@1+1.5)!', 0)
    cal.set_expression(check_input(cal.get_expression()))
    postfix = infix_to_postfix(cal.get_expression())
    result = calculate_postfix(postfix)
    assert result == 6


def test_complicated12():
    cal = Calculator('(((3!)@(2.2#!)/5)!+4)#@3', 0)
    cal.set_expression(check_input(cal.get_expression()))
    postfix = infix_to_postfix(cal.get_expression())
    result = calculate_postfix(postfix)
    assert result == 2


def test_complicated13():
    cal = Calculator('((((3!!+80)/100)#)*100/0.1)#', 0)
    cal.set_expression(check_input(cal.get_expression()))
    postfix = infix_to_postfix(cal.get_expression())
    result = calculate_postfix(postfix)
    assert result == 8


def test_complicated14():
    cal = Calculator('(((2+--3!)^2)##@(2.5^0))&2', 0)
    cal.set_expression(check_input(cal.get_expression()))
    postfix = infix_to_postfix(cal.get_expression())
    result = calculate_postfix(postfix)
    assert result == 1


def test_complicated15():
    cal = Calculator('-(((((--3!)+6)@24)!)##)', 0)
    cal.set_expression(check_input(cal.get_expression()))
    postfix = infix_to_postfix(cal.get_expression())
    result = calculate_postfix(postfix)
    assert result == -9


def test_complicated16():
    cal = Calculator('(((-3!&6)$5)^2*4)^0.5*100', 0)
    cal.set_expression(check_input(cal.get_expression()))
    postfix = infix_to_postfix(cal.get_expression())
    result = calculate_postfix(postfix)
    assert result == 1000
