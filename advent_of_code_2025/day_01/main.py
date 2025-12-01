

def part_1(data: list[str]):
    count = 0
    position = 50
    for op in data:
        if op.startswith('R'):
            position = (position + int(op[1:])) % 100
        if op.startswith('L'):
            position = (position - int(op[1:])) % 100
        if position == 0:
            count += 1

    return count


def part_2(data: list[str]):
    count = 0
    position = 50
    for op in data:
        if op.startswith('R'):
            position += int(op[1:])
            count += position // 100
            position %= 100
        if op.startswith('L'):
            # Edge case for when it is already 0
            count -= 1 if position == 0 else 0
            position = (position - int(op[1:]))
            count += abs(position) // 100
            if position <= 0: count += 1
            position %= 100

    return count


if __name__=='__main__':
    with open('day_01/data.txt') as f:
        data = f.readlines()
    
    print(part_1(data)) # 1118
    print(part_2(data)) # 6289