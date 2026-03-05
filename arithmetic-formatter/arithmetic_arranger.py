def arithmetic_arranger(problems, show_solution=False):
    if len(problems) > 5:
        return 'Error: Too many problems.'
    arranged_problems = ' '
    for problem in problems:
        num1, operator, num2 = problem.split()

        if operator not in ['+', '-']:
            return 'Error: Operator must be '+' or '-'.'
        if not (num1.isdigit() and num2.isdigit()):
            return 'Error: Numbers must only contain digits.'
        if len(num1) > 4 or len(num2) > 4:
            return 'Error: Numbers cannot be more than four digits.'
        
        width = max(len(num1), len(num2)) + 2
        formatted_problem = "{0:>{width}}\n{1}{2:>{width-1}}\n{3}\n".format(num1, operator, num2, '-' * width, width=width)
        arranged_problems += formatted_problem

    if show_solution:
        answers = ""
        for problem in problems:
            num1, operator, num2 = problem.split()
            if operator == '+':
                answer = str(int(num1) + int(num2))
            else:
                answer = str(int(num1) - int(num2))
            answers += "{0:>{width}}   ".format(answer, width=width)
        arranged_problems += answers.strip()

    return arranged_problems.rstrip()
