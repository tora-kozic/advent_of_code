
def crabs(f):
    lines = f.readlines()
    lines = lines[0].split(',')
    c = [int(i) for i in lines]
    fuel = part_two(c)
    return fuel


def part_one(c):
    c = sorted(c)
    l = len(c)
    idx = (len(c) - 1) // 2
    if l % 2 != 0:
        med = c[idx]
    else:
        med = (c[idx] + c[idx + 1]) / 2.0
    fuel = 0
    for crab in c:
        fuel += abs(crab - med)
    return fuel


def part_two(c):
    mx = max(c)
    mn = min(c)
    costs = [0] * (mx - mn)
    for i in range(mn, mx):
        for crab in c:
            n = abs(crab - i)
            cost = n * (n + 1) / 2.0
            costs[i] += cost
    return min(costs)



f = open("input.txt", "r")
x = crabs(f)
print(x)
f.close()