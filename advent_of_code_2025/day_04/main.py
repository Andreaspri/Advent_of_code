




def part_1(data):
    total = 0
    for r in range(len(data)):
        for c in range(len(data[0])):
            if data[r][c] == '@':
                # Check all 8 tiles around it
                num_close = 0
                for i, j in [
                    (r-1,c-1), # Above to the left 
                    (r,c-1),   # Directly above
                    (r+1, c-1),# Above to the right
                    (r-1, c),  # To the left
                    (r+1, c),  # To the right
                    (r-1, c+1),# Below to the left
                    (r, c+1),  # Directly below
                    (r+1, c+1) # Below to the right
                            ]:
                    try:
                        if i < 0 or j < 0:
                            continue
                        if data[i][j] == '@':
                            num_close += 1
                    except IndexError:
                        pass
                total += 1 if num_close < 4 else 0
    return total
                    


def part_2(data):
    data = [list(i) for i in data]
    total = 0
    part_total = 1
    while part_total != 0:
        part_total = 0
        for r in range(len(data)):
            for c in range(len(data[0])):
                if data[r][c] == '@':
                    # Check all 8 tiles around it
                    num_close = 0
                    for i, j in [
                        (r-1,c-1), # Above to the left 
                        (r,c-1),   # Directly above
                        (r+1, c-1),# Above to the right
                        (r-1, c),  # To the left
                        (r+1, c),  # To the right
                        (r-1, c+1),# Below to the left
                        (r, c+1),  # Directly below
                        (r+1, c+1) # Below to the right
                                ]:
                        try:
                            if i < 0 or j < 0:
                                continue
                            if data[i][j] == '@':
                                num_close += 1
                        except IndexError:
                            pass
                    if num_close < 4:
                        part_total += 1
                        data[r][c] = '.'

        total += part_total
    return total
                    

if __name__=='__main__':
    with open('day_04/data.txt') as f:
        data = f.read().split('\n')

    print(part_1(data)) # 1553
    print(part_2(data)) # 8442