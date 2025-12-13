from functools import lru_cache

def part_1(data):
    devices = {}
    for line in data:
        device, outputs = line.split(": ")
        outputs = outputs.split(" ")
        devices[device] = outputs

    def find_paths(device):
        if device == "out":
            return 1
        return sum(find_paths(d) for d in devices[device])

    return find_paths("you")



def part_2(data):
    devices = {}
    for line in data:
        device, outputs = line.split(": ")
        outputs = outputs.split(" ")
        devices[device] = outputs

    @lru_cache(maxsize=1000)
    def find_paths(device, fft, dac):
        if device == "out" and fft and dac:
            return 1
        if device == "out":
            return 0
        
        if device == "dac":
            dac = True
        if device == "fft":
            fft = True

        return sum(find_paths(d, fft, dac) for d in devices[device])

    return find_paths("svr", False, False)




if __name__=='__main__':
    with open('day_11/data.txt') as f:
        data = f.read().splitlines()


    print(part_1(data)) # 423
    print(part_2(data)) # 333657640517376


