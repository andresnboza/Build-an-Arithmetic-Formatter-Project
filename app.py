def evaluate_digits(num):
    num_digits = len(str(num))
    if num_digits > 4:
        raise ValueError("Error: Numbers cannot be more than four digits.")


def get_solution(first, last, sign):
    if sign not in ["+", "-"]:
        raise ValueError("Error: Operator must be '+' or '-'.")

    try:
        num1 = int(first)
        evaluate_digits(num1)

        num2 = int(last)
        evaluate_digits(num2)
    except ValueError:
        raise ValueError("Error: Numbers must only contain digits.")

    if sign == "+":
        return num1 + num2
    elif sign == "-":
        return num1 - num2


def get_texts(elements, show_answers):
    if len(elements) == 3:
        first = elements[0]
        sign = elements[1]
        last = elements[-1]

        width = max(len(first), len(last)) + 2

        top = first.rjust(width)
        bottom = sign + last.rjust(width - 1)
        base = "-" * width
        
        result_line = ""
        if show_answers:
            arithmetic_result = get_solution(first, last, sign)
            if arithmetic_result is not None:
                result_line = str(arithmetic_result).rjust(width)

        return [top, bottom, base, result_line]
    
    return []


def create_fix_matrix(elements):
    rows = len(elements)
    cols = 4
    initial_value = "" 
    matrix = [[initial_value for _ in range(cols)] for _ in range(rows)]
    return matrix


def get_printable_final_result(matrix, show_answers):
    top = ""
    bottom = ""
    base = ""
    result = ""

    for operation in matrix:
        top += operation[0] + "    " 
        bottom += operation[1] + "    "
        base += operation[2] + "    "
        result += operation[3] + "    "

    final_result = top.rstrip() + "\n" + bottom.rstrip() + "\n" + base.rstrip()
    
    if show_answers:
        final_result += "\n" + result.rstrip()

    return final_result


def arithmetic_arranger(problems, show_answers=False):

    if len(problems) > 5:
        return "Error: Too many problems."

    try:
        formatted_problems = []
        for operation in problems:
            elements = operation.split()
            if len(elements) != 3:
                return "Error: Invalid problem format."

            first, sign, last = elements

            if sign not in ["+", "-"]:
                return "Error: Operator must be '+' or '-'."

            if not first.isdigit() or not last.isdigit():
                return "Error: Numbers must only contain digits."
            
            if len(first) > 4 or len(last) > 4:
                return "Error: Numbers cannot be more than four digits."

            formatted_problems.append(get_texts(elements, show_answers))

        final_result = get_printable_final_result(formatted_problems, show_answers)
        return final_result
    

    except Exception as e:
        return str(e)

print(f'{arithmetic_arranger(["3801 - 2", "123 + 49"])}')