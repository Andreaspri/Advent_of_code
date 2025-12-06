import re



def part_1(data):
    total = 0
    for p_range in data:
        start, stop = p_range.split("-")
        for num in range(int(start), int(stop)+1):
            if len(str(num)) % 2 == 0 and str(num)[len(str(num))//2:] == str(num)[:len(str(num))//2]:
                total += num
    return total
    

def part_2(data):
    total = 0
    for p_range in data:
        start, stop = p_range.split("-")
        for num in range(int(start), int(stop)+1):
            str_num = str(num)
            num_len = len(str_num)
            for i in range(0, num_len//2):
                occ = re.findall(str_num[:i+1], str_num)
                if len("".join(occ)) == num_len:
                    total += num
                    break
    return total


if __name__ == "__main__":
    with open("day_02/data.txt") as f:
        data = f.read().split(',')
    print(part_1(data)) # 23701357374
    print(part_2(data)) # 34284458938