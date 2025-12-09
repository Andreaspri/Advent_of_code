import numpy as np


def find_distances(data):
    points = [tuple(map(int,point.split(','))) for point in data]
    distances = []
    for i in range(len(points)):
        for j in range(i+1,len(points)):
            if i == j:
                continue
            x_1 = points[i][0]
            y_1 = points[i][1]
            z_1 = points[i][2]

            x_2 = points[j][0]
            y_2 = points[j][1]
            z_2 = points[j][2]
            dist = np.sqrt((x_1-x_2)**2 + (y_1-y_2)**2 + (z_1-z_2)**2)

            distances.append((dist,(points[i],points[j])))


    return sorted(distances, key=lambda x: x[0])


def part_1(distances, num_conns=1000):
    circuits = []

    for _, p in distances[:num_conns]:
        p1 = p[0]
        p2 = p[1]
        temp_c = []

        # Find all circuits they are already in
        for c in circuits:
            if p1 in c or p2 in c:
                temp_c.append(c)
        
        # Remove them from the circuits and make a new circuit
        new_c = {p1,p2}
        for c in temp_c:
            circuits.remove(c)
            new_c |= c 

        circuits.append(new_c)

    circuits = sorted(circuits, key=lambda x: len(x), reverse=True)

    return len(circuits[0]) * len(circuits[1]) * len(circuits[2])


def part_2(distances, num_points):
    circuits = []

    for _, p in distances:
        p1 = p[0]
        p2 = p[1]
        temp_c = []

        # Find all circuits they are already in
        for c in circuits:
            if p1 in c or p2 in c:
                temp_c.append(c)
        
        # Remove them from the circuits and make a new circuit
        new_c = {p1,p2}
        for c in temp_c:
            circuits.remove(c)
            new_c |= c 

        circuits.append(new_c)

        if len(circuits) == 1 and len(circuits[0]) == num_points:
            return p1[0] * p2[0]


if __name__=='__main__':
    with open('day_08/data.txt') as f:
        data = f.read().splitlines()

    distances = find_distances(data)

    print(part_1(distances,1000))       # 244188
    print(part_2(distances, len(data))) # 8361881885