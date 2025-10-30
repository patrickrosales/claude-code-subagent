# Calculator - Claude Code Subagent Demo

A demonstration of Claude Code's subagent capabilities for verification and testing. This project implements a simple calculator library with basic arithmetic operations and expression evaluation.

## Features

- **Basic Arithmetic Operations**: Add, subtract, multiply, and divide
- **Expression Evaluation**: Parse and evaluate mathematical expressions from strings with proper operator precedence
- **Input Validation**: Comprehensive validation of mathematical expressions
- **Type Safety**: Full type hints throughout the codebase
- **Well-Tested**: Comprehensive test suite covering all functionality

## Installation

### Prerequisites

- Python 3.8 or higher
- pip

### Setup

```bash
# Clone the repository
git clone <repository-url>
cd claude-code-subagent

# Install the package and dependencies
pip install -e .
```

This will install the package in development mode along with required testing and linting tools (pytest and flake8).

## Usage

### Basic Arithmetic Operations

```python
from src.calculator import add, subtract, multiply, divide

# Addition
result = add(2, 3)  # Returns 5

# Subtraction
result = subtract(5, 3)  # Returns 2

# Multiplication
result = multiply(2, 3)  # Returns 6

# Division
result = divide(10, 2)  # Returns 5.0
```

### Expression Evaluation

```python
from src.calculator import calculate_expression

# Simple expressions
result = calculate_expression("2 + 3")  # Returns 5
result = calculate_expression("6 / 3")  # Returns 2

# Complex expressions with operator precedence
result = calculate_expression("2 + 3 * 4")  # Returns 14 (3*4 evaluated first)

# Expressions with parentheses
result = calculate_expression("(2 + 3) * 4")  # Returns 20

# Whitespace is handled automatically
result = calculate_expression(" 2 + 3 ")  # Returns 5
```

### Error Handling

```python
from src.calculator import divide, calculate_expression

# Division by zero
try:
    divide(5, 0)
except ValueError as e:
    print(f"Error: {e}")

# Invalid expressions
try:
    calculate_expression("2 + * 3")
except ValueError as e:
    print(f"Error: {e}")  # ValueError: Invalid operator sequence

try:
    calculate_expression("2 + 3)")
except ValueError as e:
    print(f"Error: {e}")  # ValueError: Mismatched parentheses
```

## Testing

Run the test suite to verify all functionality:

```bash
# Run all tests
pytest tests/

# Run tests with verbose output
pytest tests/ -v

# Run specific test class
pytest tests/test_calculator.py::TestCalculatorBasic -v

# Run with coverage
pytest tests/ --cov=src
```

The test suite includes:
- **TestCalculatorBasic**: Tests for basic arithmetic operations
- **TestCalculatorExpression**: Tests for expression evaluation, precedence, and validation

## Code Quality

Lint the codebase to ensure it follows PEP 8 style guidelines:

```bash
flake8 src tests
```

## Code Standards

This project follows these standards:

- **Python Version**: Python 3.8+
- **Style Guide**: PEP 8
- **Type Hints**: All functions have type hints for parameters and return values
- **Docstrings**: Comprehensive docstrings following Google style format
- **Error Handling**: Explicit error handling with descriptive messages

## Project Structure

```
claude-code-subagent/
├── src/
│   └── calculator.py          # Main calculator module
├── tests/
│   └── test_calculator.py     # Test suite
├── setup.py                   # Project setup and dependencies
├── CLAUDE.md                  # Claude Code development instructions
└── README.md                  # This file
```

## Development Workflow

This project demonstrates a test-driven development approach with Claude Code:

1. **Write Tests**: Create failing test cases for desired functionality
2. **Implement Solutions**: Write code to make tests pass
3. **Verify with Subagents**: Use Claude Code's subagent capabilities for verification
4. **Iterate**: Refine implementation based on verification results
5. **Commit**: Commit the complete solution

## API Reference

### Functions

#### `add(a: Union[int, float], b: Union[int, float]) -> Union[int, float]`
Returns the sum of two numbers.

#### `subtract(a: Union[int, float], b: Union[int, float]) -> Union[int, float]`
Returns the difference of two numbers (a - b).

#### `multiply(a: Union[int, float], b: Union[int, float]) -> Union[int, float]`
Returns the product of two numbers.

#### `divide(a: Union[int, float], b: Union[int, float]) -> float`
Returns the quotient of two numbers (a / b).
- **Raises**: `ValueError` if b is zero

#### `calculate_expression(expression: str) -> Union[int, float]`
Evaluates a mathematical expression string.
- **Supports**: Basic arithmetic operators (+, -, *, /) and parentheses
- **Precedence**: Follows standard mathematical operator precedence (multiplication/division before addition/subtraction)
- **Raises**: `ValueError` for invalid or malformed expressions

## License

This project is part of the Claude Code demonstration. See the repository for license information.

## Contributing

This is a demonstration project for Claude Code subagent capabilities. For contributions or modifications, follow the development workflow outlined in the CLAUDE.md file.
