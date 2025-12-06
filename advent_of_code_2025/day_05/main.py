

def part_1(data):
    ranges, ingredients = data.split("\n\n")
    total = 0
    for ingredien in ingredients.split("\n"):
        for r in ranges.split("\n"):
            start, stop = r.split("-")
            start, stop = int(start), int(stop)
            if start <= int(ingredien) <= stop:
                total += 1
                break

    return total



def part_2(data):
    total = 0
    ranges = sorted([(int(r.split("-")[0]), int(r.split("-")[1])) for r in data.split("\n\n")[0].split("\n")], key=lambda x: x[0])
    current_end = 0
    for start, stop in ranges:
        start = current_end if current_end > start else start
        if start > stop:
            continue
        total += stop+1 - start
        current_end = stop+1

    return total





if __name__=='__main__':
    with open('day_05/data.txt') as f:
        data = f.read()

    print(part_1(data)) # 598
    print(part_2(data)) # 360341832208407