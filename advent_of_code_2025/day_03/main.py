


def part_1(data):
    total = 0
    for bank in data:
        high = 0
        for i in range(len(bank)):
            for j in range(i+1, len(bank)):
                if int(bank[i] + bank[j]) > high:
                    high = int(bank[i] + bank[j])
        total += high

    return total


def part_2(data):
    total = 0
    for bank in data:
        batteries = []
        curr_bank = list(bank)
        while len(batteries) < 12:
            max_value = max(curr_bank[:len(batteries)-11 if len(batteries)-11 < 0 else len(curr_bank)])
            index = curr_bank.index(max_value)
            batteries.append(max_value)
            curr_bank = curr_bank[index+1:]
                
        total += int("".join(batteries))

    return total



if __name__=='__main__':
    with open('day_03/data.txt') as f:
        data = f.read().split('\n')

    print(part_1(data)) # 16812
    print(part_2(data)) # 166345822896410