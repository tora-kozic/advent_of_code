
LOWERCASE_ASCII_ADJ=96
UPPERCASE_ASCII_ADJ=38

def part_one(lines):
    priorities = []
    for l in lines:
        l = l.strip()
        if len(l) % 2 == 0:
            end1 = p2 = len(l)//2
        else:
            end1 = p2 = len(l)//2+1
        p1 = 0
        while p1 < end1:
            res = helper(l, p1, p2)
            if res:
                priorities.append(
                    ord(res)-LOWERCASE_ASCII_ADJ if ord(res) > 95 else ord(res)-UPPERCASE_ASCII_ADJ
                )
                break
            p1 += 1

    return sum(priorities)


def helper(l, p1, p2):
    while p2 < len(l):
        if l[p1] == l[p2]:
            return l[p1]
        p2 += 1
    return None


def part_two(lines):
    priorities = []
    for i in range(0, len(lines)-1, 3):
        group = [l.strip() for l in lines[i:i+3]]
        for c in group[0]:
            if c in group[1] and c in group[2]:
                priorities.append(
                    ord(c) - LOWERCASE_ASCII_ADJ if ord(c) > 95 else ord(c) - UPPERCASE_ASCII_ADJ
                )
                break
    return sum(priorities)
