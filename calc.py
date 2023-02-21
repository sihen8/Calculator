def is_integer(n):
    try:
        float(n)
    except ValueError:
        return False
    else:
        return float(n).is_integer()

def format_equation(equation):

    equation_list = []
    number = False
    last_term = ''
 
    for i in range(len(equation)):

        #TEST
        #print("cycle: " + str(i))
        #print("Last term: " + str(last_term))
        #print("Last value was a number?: " + str(number))
        #print(equation_list)
        #print()
        #TEST

        if is_integer(equation[i]) == True:
            if number == True:
                equation_list[len(equation_list) - 1] = int(str(last_term) + str(equation[i]))
            else:
                equation_list.append(int(equation[i]))

            number = True
            last_term = str(last_term) + str(equation[i])

        else:
            equation_list.append(equation[i])
            last_term = ""
            number = False

    print(equation_list)
    for i in equation_list:
        if equation_list[i] == ".":
            equation_list[i - 1] = str(equation_list[i - 1]) + "." + str(equation_list[i + 1])
            equation_list.pop(i)
            equation_list.pop(i)
    return equation_list


print(format_equation("1.25"))





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

