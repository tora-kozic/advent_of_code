
def get_position(f):
    forward = 0
    depth = 0
    lines = f.readlines()
    for line in lines:
        words = line.split()
        d = words[0]
        if d == "forward":
            forward += int(words[1])
        elif d == "up":
            depth -= int(words[1])
        else:  # down
            depth += int(words[1])
    return forward * depth

def get_aim(f):
    forward = 0
    depth = 0
    aim = 0
    lines = f.readlines()
    for line in lines:
        words = line.split()
        d, v = words
        v = int(v)
        if d == "forward":  # increases horiz pos by X, increases depth by aim * X
            forward += v
            depth += (aim * v)
        elif d == "up":  # decreases aim by X
            aim -= v
        else:  # down - increases aim by X
            aim += v
    return forward * depth


f = open("input.txt", "r")
print(get_aim(f))
