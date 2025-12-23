import re
import numpy as np




def part_1(data):
    count = 0
    raw_presents = re.findall(r"\d+:\n[.|#|\n]+", data)
    raw_tree_grids = re.findall(r"\d+x\d+: [ |\d]+", data)
    presents = {}
    for p in raw_presents:
        i_p , shape = p.split(":\n")
        presents[int(i_p)] = np.array([[1 if c == '#' else 0 for c in r]for r in shape.removesuffix("\n\n").split("\n")])

    grid_amounts = []
    for g in raw_tree_grids:
        grid, num_presents = g.split(": ")
        grid_amounts.append((tuple(map(int,grid.split("x"))), tuple(map(int,num_presents.split(" ")))))

    for grid, amounts in grid_amounts:
        space = grid[0] * grid[1]
        space_req = 0
        for i, amount in enumerate(amounts):
            present: np.ndarray = presents[i]
            space_req += present.sum() * amount
        
        if space_req < space:
            count += 1


    return count



if __name__=='__main__':
    with open('day_12/data.txt') as f:
        data = f.read()

    print(part_1(data)) # 565
    # Only 1 part this day