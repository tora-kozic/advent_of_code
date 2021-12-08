
# 1 - 2 segments
# 4 - 4 segments
# 7 - 3 segments
# 8 - 7 segments

def numbers(f):
    vals = []
    lines = f.readlines()
    lines = [line.split('|') for line in lines]
    for i in range(len(lines)):
        lines[i] = [(line.strip()).split(' ') for line in lines[i]]
        # for j in lines[i][1]:
        #     _sum += 1 if len(j) in unique_numbers else 0
        vals.append(cipher(lines[i][0], lines[i][1]))
    return sum(vals)


# decipher mapping m into final value n
def cipher(m, n):
    val = [''] * 4
    unique_numbers = {2: '1', 4: '4', 3: '7', 7: '8'}

    # build dict for values used for deciphering
    d = {}
    for v in m:
        if len(v) == 2:
            d[1] = v
        elif len(v) == 4:
            d[4] = v
        else:
            continue

    # determine final value
    for i in range(len(n)):
        l = len(n[i])
        if l in unique_numbers:
            val[i] = unique_numbers[l]
        elif l == 5:
            val[i] = five(d, n[i])
        elif l == 6:
            val[i] = six(d, n[i])

    total = ''
    for digit in val:
        total += digit
    return int(total)


def five(d, n):
    in_four = 0
    in_one = 0
    for i in n:
        if i in d[4]:
            in_four += 1
        if i in d[1]:
            in_one += 1
    if in_four == 2:
        return '2'
    elif in_one == 2:
        return '3'
    else:
        return '5'


def six(d, n):
    in_four = 0
    in_one = 0
    for i in n:
        if i in d[4]:
            in_four += 1
        if i in d[1]:
            in_one += 1
    if in_one == 1:
        return '6'
    elif in_four == 4:
        return '9'
    else:
        return '0'


f = open("input.txt", "r")
x = numbers(f)
print(x)
f.close()
