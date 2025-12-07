from functools import lru_cache



def part_1(data):
    # Start by finding the S which is where the beam starts
    start = data[0].find('S')
    beams = set([start])
    splits = 0
    for r in range(len(data[1:])):
        for c in range(len(data[r])):
            if data[r][c] == '^' and c in beams:
                    beams.add(c-1)
                    beams.add(c+1)
                    beams.remove(c)
                    splits += 1
    return splits



def part_2(data):
    start = data[0].find('S')
    data = data[1:]

    @lru_cache()
    def follow_path(r, c):
        if r >= len(data):
            return 1
        
        if data[r][c] == '^':
            return follow_path(r+1, c+1) + follow_path(r+1, c-1)
        else:
            return follow_path(r+1, c)

    return follow_path(1, start)



if __name__=='__main__':
    with open('day_07/data.txt') as f:
        data = f.read().splitlines()

    print(part_1(data)) # 1598
    print(part_2(data)) # 4509723641302