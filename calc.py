def simplify(equation_list):
    pemdas = 0
    counter = 0
    while len(equation_list) != 1:
        if equation_list[counter] == '(':
            parenthesis = []
            counter += 1
            while equation_list[counter] != ')':
                parenthesis.append(equation_list[counter])
                equation_list.pop(counter)
            parenthesis = simplify(parenthesis)
            parenthesis = parenthesis[0]
            equation_list.insert(counter, parenthesis)
            equation_list.pop(counter - 1)
            equation_list.pop(counter)
        if equation_list[counter] == '^' and pemdas == 1:
            equation_list[counter - 1] = equation_list[counter - 1] ** equation_list[counter + 1]
            equation_list.pop(counter)
            equation_list.pop(counter)
            counter = 0
        elif equation_list[counter] == '*' and pemdas == 2:
            equation_list[counter - 1] = equation_list[counter - 1] * equation_list[counter + 1]
            equation_list.pop(counter)
            equation_list.pop(counter)
            counter = 0
        elif equation_list[counter] == '/' and pemdas == 2:
            equation_list[counter - 1] = equation_list[counter - 1] / equation_list[counter + 1]
            equation_list.pop(counter)
            equation_list.pop(counter)
            counter = 0
        elif equation_list[counter] == '+' and pemdas == 3:
            equation_list[counter - 1] = equation_list[counter - 1] + equation_list[counter + 1]
            equation_list.pop(counter)
            equation_list.pop(counter)
            counter = 0
        elif equation_list[counter] == '-' and pemdas == 3:
            equation_list[counter - 1] = equation_list[counter - 1] - equation_list[counter + 1]
            equation_list.pop(counter)
            equation_list.pop(counter)
            counter = 0
        elif counter == len(equation_list) - 1:
            pemdas += 1
            counter = 0
        counter += 1
    return(equation_list)

def format_equation(equation):
    equation_list = []
    number = False
    last_term = ''
    for i in range(len(equation)):
        try:
            if number == True:
                equation_list[i - 1] = int(str(last_term) + equation[i])
            else:
                equation_list.append(int(equation[i]))
            number = True
            last_term = equation[i]
        except:
            equation_list.append(equation[i])
            last_term = equation[i]
            number = False
    return equation_list