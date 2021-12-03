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


