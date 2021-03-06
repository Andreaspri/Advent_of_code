

def part_1():
    with open("data.txt") as f:
        data = [int(i) for i in f.read().split(",")]

    return min([sum([abs(crab-i) for crab in data]) for i in range(min(data),max(data))])


def part_2():
    with open("data.txt") as f:
        data = [int(i) for i in f.read().split(",")]

    return min([sum([abs((crab-i))*(abs(crab-i) + 1)/2 for crab in data]) for i in range(min(data), max(data))])


if __name__ == '__main__':
    print(part_1())
    print(part_2())


