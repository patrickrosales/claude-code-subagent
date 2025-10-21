"""
Calculator module providing basic arithmetic operations and expression evaluation.

This module implements basic arithmetic operations (add, subtract, multiply, divide)
and a calculate_expression function that evaluates string mathematical expressions.
"""

from typing import Union


def add(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """
    Add two numbers.

    Args:
        a: First number
        b: Second number

    Returns:
        Sum of a and b
    """
    return a + b


def subtract(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """
    Subtract b from a.

    Args:
        a: Number to subtract from
        b: Number to subtract

    Returns:
        Difference of a and b
    """
    return a - b


def multiply(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """
    Multiply two numbers.

    Args:
        a: First number
        b: Second number

    Returns:
        Product of a and b
    """
    return a * b


def divide(a: Union[int, float], b: Union[int, float]) -> float:
    """
    Divide a by b.

    Args:
        a: Numerator
        b: Denominator

    Returns:
        Quotient of a and b

    Raises:
        ValueError: If b is zero
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def calculate_expression(expression: str) -> Union[int, float]:
    """
    Evaluate a mathematical expression string.

    Supports basic arithmetic operators (+, -, *, /) and parentheses.
    Follows standard operator precedence (multiplication/division before addition/subtraction).

    Args:
        expression: String containing the mathematical expression

    Returns:
        Result of the evaluated expression

    Raises:
        ValueError: If the expression is invalid or malformed
    """
    # Remove whitespace
    expression = expression.strip()

    if not expression:
        raise ValueError("Empty expression")

    # Validate expression has valid characters
    valid_chars = set('0123456789+-*/(). ')
    if not all(c in valid_chars for c in expression):
        raise ValueError("Invalid characters in expression")

    # Check for invalid operator sequences (e.g., "2 + * 3")
    # This is a basic check - operators shouldn't appear consecutively except after (
    operators = '+-*/'
    for i in range(len(expression) - 1):
        if expression[i] in operators and expression[i + 1] in operators:
            raise ValueError("Invalid operator sequence")

    # Check for mismatched parentheses
    paren_count = 0
    for char in expression:
        if char == '(':
            paren_count += 1
        elif char == ')':
            paren_count -= 1
            if paren_count < 0:
                raise ValueError("Mismatched parentheses")

    if paren_count != 0:
        raise ValueError("Mismatched parentheses")

    # Use Python's eval for expression evaluation
    # Note: This is safe here because we've validated the input to only contain
    # numeric and mathematical operator characters
    try:
        result = eval(expression)
        return result
    except SyntaxError:
        raise ValueError("Invalid expression syntax")
    except ZeroDivisionError:
        raise ValueError("Division by zero in expression")
    except Exception as e:
        raise ValueError(f"Error evaluating expression: {str(e)}")
