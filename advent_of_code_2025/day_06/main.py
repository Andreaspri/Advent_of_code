import re
import numpy as np



def part_1(data):
    total = 0
    data = [re.findall("\\d+|[+,*]",row) for row in data.split('\n')]
    operators = data.pop()
    array = np.array(data, dtype=int)
    t_array = array.transpose()
    for arr, op in zip(t_array, operators):
        if op == '+':
            total += np.sum(arr)
        elif op == '*':
            total += np.prod(arr)
    return total


def part_2(data):
    total = 0
    data = data.split("\n")
    operators = data.pop()
    number_start = []
    i = 0
    # Use the operator row to find the start index of each number
    for i, c in enumerate(operators):
        if c in ('*', '+'):
            number_start.append(i)
    # Also add the last index + 1 since that would be the end of the number
    number_start.append(i+1)

    for pos, op in zip(range(len(number_start)-1), re.findall("[+,*]",operators)):
        start = number_start[pos]
        stop = number_start[pos+1]
        current_numbers = []
        for n in range(start, stop):
            num = ""
            for row in data:
                if row[n].isdigit():
                    num += row[n]
            if num:
                current_numbers.append(int(num))

        if op == '+':
            total += np.sum(current_numbers)
        elif op == '*':
            total += np.prod(current_numbers)

    return total

if __name__=='__main__':
    with open('day_06/data.txt') as f:
        data = f.read()

    print(part_1(data)) # 5784380717354
    print(part_2(data)) # 7996218225744