
def part_one(lines):
    count = 0
    for l in lines:
        vals = []
        for v in l.split(","):
            val = v.strip().split('-')
            vals.append([int(x) for x in val])
        if helper(vals[0], vals[1]):
            count += 1
    return count


def helper(r1, r2):
    """
    check if one range overlaps with another.
    """
    if r1[0] == r2[0] or r1[1] == r2[1]:
        return True
    if r1[0] < r2[0] and r1[1] < r2[0]:
        return False
    if r1[0] > r2[1] and r1[1] > r2[1]:
        return False
    return True

