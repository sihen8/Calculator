def is_float(n):
    try:
        float(n)
        return(True)
    except ValueError:
        return False

def strToList(equation):

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

        if is_float(equation[i]) == True:
            if number == True:                
                equation_list[len(equation_list) - 1] = str(last_term) + str(equation[i])
            else:
                equation_list.append(str(equation[i]))

            number = True
            last_term = str(last_term) + str(equation[i])

        else:
            equation_list.append(equation[i])
            last_term = ""
            number = False
    return equation_list

def floatify(equation_list):
    things_to_delete = 0
    for i in range(len(equation_list)):
        if equation_list[i] == ".":
            equation_list[i - 1] = equation_list[i - 1] + "." + equation_list[i + 1]
            equation_list[i] = "DELETE THIS"
            equation_list[i + 1] = "DELETE THIS"
            things_to_delete += 2

    counter = 0
    while things_to_delete != 0:
        if equation_list[counter] == "DELETE THIS":
            equation_list.pop(counter)
            counter -= 1
            things_to_delete -= 1
        counter += 1

    for i in range(len(equation_list)):
        if is_float(equation_list[i]) == True:
            equation_list[i] = float(equation_list[i])
    return equation_list

    



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

def solve_this(equation):
    equation_list = strToList(equation)
    equation_list = floatify(equation_list)
    answer = simplify(equation_list)
    return answer
