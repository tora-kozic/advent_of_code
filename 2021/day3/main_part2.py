def generate_rates(f):
    # split numbers by most common digit
    lines = f.readlines()
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
power = generate_rates(f)
print(power)
