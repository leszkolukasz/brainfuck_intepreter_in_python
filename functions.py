def clean_code(txt):
    allowed = ['<', '>', '-', '+', ',', '.', '[', ']']
    return [v for v in txt if v in allowed]

def create_bracket_shifts(txt):
    stack, brackets = [], {}

    for i, v, in enumerate(txt):
        if v == '[':
            stack.append(i)

        elif v == ']':
            if(len(stack) == 0):
                raise Exception('ERROR: Too many closing brackets')

            else:
                brackets[i] = stack[-1]
                brackets[stack[-1]] = i
                stack.pop()

    if len(stack) > 0:
        raise Exception('ERROR: Too many opening brackets')

    return brackets

def execute(txt, shift):
    pointer, cells, i = 0, [0]*256, 0
    print_warning = True

    while i < len(txt):
        cmd = txt[i]

        if cmd == '<':
            pointer -= 1
            if pointer < 0:
                print(i)
                print(cells)
                raise Exception('ERROR: Instruction pointer has reached forbidden cell')

        if cmd == '>':
            pointer += 1
            if pointer == len(cells):
                cells.append(0)

        if cmd == '+':
            cells[pointer] += 1
            if cells[pointer] > 255 and print_warning:
                print('WARNING: Cell {} holds value of more than 255. If you don\'t want to see this warning change variable print_warning to false'.format(pointer))

        if cmd == '-':
            cells[pointer] -= 1
            if cells[pointer] < 0 and print_warning:
                print('WARNING: Cell {} holds negative value. If you don\'t want to see this warning change variable print_warning to false'.format(pointer))

        if cmd == ',':
            val = int(input())
            if val < 0 or val > 255:
                raise Exception('ERROR: Non-char value given as input')

            cells[pointer] = val

        if cmd == '.':
            if cells[pointer] < 0 or cells[pointer] > 255:
                raise Exception('ERROR: Non-char value cannot be written')

            print(chr(cells[pointer]), end='')

        if cmd == '[' and cells[pointer] == 0:
            i = shift[i]

        if cmd == ']' and cells[pointer] != 0:
            i = shift[i]

        i += 1 