import shapely



def part_1(data):
    points = [tuple(map(int,point.split(','))) for point in data]
    areas = []
    for i in range(len(points)):
        for j in range(i+1,len(points)):
            if i == j:
                continue
            x_1 = points[i][0]
            y_1 = points[i][1]

            x_2 = points[j][0]
            y_2 = points[j][1]
            area = (abs(x_1-x_2)+1) * (abs(y_1-y_2)+1)

            areas.append(area)

    return sorted(areas, reverse=True)[0]


def part_2(data):
    red_points = [tuple(map(int,point.split(','))) for point in data]
    valid_points = set()
    areas = []

    for i in range(len(red_points)):
        for j in range(i+1,len(red_points)):
            if i == j:
                continue
            x_1 = red_points[i][0]
            y_1 = red_points[i][1]

            x_2 = red_points[j][0]
            y_2 = red_points[j][1]

            area = (abs(x_1-x_2)+1) * (abs(y_1-y_2)+1)

            areas.append((area,(red_points[i], red_points[j])))

            if x_1 == x_2:
                valid_points |= set(zip([x_1]*(abs(y_1-y_2)+1), range(min(y_1, y_2),max(y_1,y_2)+1)))
            if y_1 == y_2:
                valid_points |= set(zip(range(min(x_1, x_2),max(x_1,x_2)+1), [y_1]*(abs(x_1-x_2)+1)))



    start = valid_points.pop()
    polygon_list = [start]
    while valid_points:
        x, y = polygon_list[-1]
        
        neighbors = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
        
        found = False
        for neighbor in neighbors:
            if neighbor in valid_points:
                polygon_list.append(neighbor)
                valid_points.remove(neighbor)
                found = True
                break
        
        if not found:
            break

    # Feels like cheating
    polygon = shapely.Polygon(polygon_list)
    shapely.prepare(polygon)

    areas = sorted(areas, key=lambda x: x[0], reverse=True)
    for area, p in areas:
        x_1 = p[0][0]
        y_1 = p[0][1]

        x_2 = p[1][0]
        y_2 = p[1][1]

        if polygon.covers(shapely.geometry.box(minx=min(x_1,x_2), miny=min(y_1,y_2), maxx=max(x_1,x_2), maxy=max(y_1,y_2))):
            return area



if __name__=='__main__':
    with open('day_09/data.txt') as f:
        data = f.read().splitlines()


    print(part_1(data)) # 4744899849
    print(part_2(data)) # 1540192500 # Takes 181 seconds to run, all time is consumed by shapely polygon.covers