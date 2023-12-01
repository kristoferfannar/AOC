FILE = 'input.txt'


def read_lines_to_list():
    lines = [] 
    
    with open(FILE, 'r') as f:
        lines = f.readlines()

    return ''.join(lines).split('\n\n')


def get_answer_from_lines():
    lines = read_lines_to_list()

    elf_sum = []

    for line in lines:

        cals = line.split('\n')
        elf_sum.append(sum([int(num) for num in cals if num != '']))

    return max(elf_sum)


print(get_answer_from_lines())
