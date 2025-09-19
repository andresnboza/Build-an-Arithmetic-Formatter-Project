# Arithmetic Formatter

A Python program that formats arithmetic problems in a visually appealing vertical layout, similar to how you might solve them on paper.

## Features

- Formats addition and subtraction problems vertically
- Supports up to 5 problems at once
- Optional display of answers
- Input validation with clear error messages
- Proper spacing and alignment

## How It Works

The program takes a list of arithmetic problems as strings and formats them vertically. For example:

**Input:** `["32 + 698", "3801 - 2", "45 + 7", "123 + 49"]`

**Output:**
```
   32      3801      45      123
+ 698    -    2    +  7    +  49
-----    ------    ----    -----
```

**With answers:**
```
   32      3801      45      123
+ 698    -    2    +  7    +  49
-----    ------    ----    -----
  730      3799      52      172
```

## Usage

### Basic Usage

```python
from app import arithmetic_arranger

# Format problems without answers
result = arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 7", "123 + 49"])
print(result)

# Format problems with answers
result = arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 7", "123 + 49"], True)
print(result)
```

### Function Signature

```python
arithmetic_arranger(problems, show_answers=False)
```

**Parameters:**
- `problems` (list): A list of strings representing arithmetic problems
- `show_answers` (bool, optional): Whether to display the calculated answers. Default is `False`

**Returns:**
- `str`: Formatted arithmetic problems or error message

## Input Requirements

### Valid Input Format
- Each problem must be a string with the format: `"number operator number"`
- Operators must be `+` or `-`
- Numbers must contain only digits
- Numbers cannot exceed 4 digits
- Maximum of 5 problems per function call

### Examples of Valid Input
```python
["32 + 698"]
["123 - 45", "67 + 89"]
["1234 + 5678", "999 - 111", "42 + 58"]
```

### Examples of Invalid Input
```python
["32 * 698"]           # Invalid operator
["32 + 69a"]          # Non-digit character
["12345 + 67"]        # Number exceeds 4 digits
["32 +"]              # Missing operand
```

## Error Handling

The program provides clear error messages for various invalid inputs:

- **Too many problems:** "Error: Too many problems." (more than 5)
- **Invalid operator:** "Error: Operator must be '+' or '-'."
- **Non-digit numbers:** "Error: Numbers must only contain digits."
- **Numbers too large:** "Error: Numbers cannot be more than four digits."
- **Invalid format:** "Error: Invalid problem format."

## Code Structure

The program consists of several helper functions:

- `arithmetic_arranger()`: Main function that orchestrates the formatting
- `get_texts()`: Formats individual arithmetic problems
- `get_solution()`: Calculates the arithmetic result
- `evaluate_digits()`: Validates number length
- `create_fix_matrix()`: Creates a matrix structure for formatting
- `get_printable_final_result()`: Combines formatted problems into final output

## Running the Code

To run the example included in the file:

```bash
python app.py
```

This will output:
```
 3801      123
-   2    +  49
-----    -----
```

## Requirements

- Python 3.x
- No external dependencies required

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is open source and available under the [MIT License](LICENSE).