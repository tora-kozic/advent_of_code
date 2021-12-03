# calc gamma rate and epsilon rate
def generate_rates(f):
    lines = f.readlines()
    # find length of binary - l
    l = len(lines[0]) - 1
    # find numbers of lines - n
    n = len(lines)
    # create array size l
    a = [0] * l
    # store total of numbers in each array
    for line in lines:
        for i in range(len(line) - 1):
            a[i] += int(line[i])
    # if sum of index > n/2, take 1, else 0
    # convert array from binary into decimal
    # x = ""
    # for v in a:
    #     x += '1' if v > (n/2) else '0'
    # return x
    g = ""
    e = ""
    for v in a:
        flag = v > (n/2)
        g += '1' if flag else '0'
        e += '0' if flag else '1'
    p = int(g, 2) * int(e, 2)
    return p


def generate_rates_two(f):
    # split numbers by most common digit
    lines = f.readlines()
    #l = len(lines[0]) - 1
    c = helper(lines, 0)
    o = helper(lines, 0, common=False)
    p = int(c, 2) * int(o, 2)
    return p


def helper(lines, n, common=True):
    # split numbers by most common (if common=true) digit in Nth place
    digit = find_most_common(lines, n)
    if not common:
        digit = not digit
    looking = '1' if digit else '0'
    # return new list
    x = []
    for line in lines:
        if line[n] == looking:
            x.append(line)
    # recurse on new list with n + 1
    if len(x) == 1:
        return x[0]
    return helper(x, n+1, common)


def find_most_common(lines, n):
    a = 0
    l = len(lines)
    # could stop count early if by value is determined by halfway point
    for line in lines:
        a += int(line[n])
    return 1 if a >= l/2 else 0

f = open('input.txt', 'r')
power = generate_rates_two(f)
print(power)
