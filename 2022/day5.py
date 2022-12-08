
def part_one(f):
    crates = []
    # read in starting crate config
    l = f.readline()
    while l != '\n':
        # if l == '\n':
        #     break
        stack = 1
        for i in range(1, len(l), 4):
            if ord(l[i]) > 64 and ord(l[i]) < 91:
                try:
                    crates[stack-1].append(l[i])
                except IndexError:
                    for j in range(len(crates), stack):
                        crates.append([])
                    crates[stack-1].append(l[i])
            stack += 1
        l = f.readline()

    # read instructions
    l = f.readline()
    while l:
        l = l.split()
        num, start, end = int(l[1]), int(l[3]), int(l[5])
        # PART ONE
        # for i in range(num):
        #     crates[end-1].insert(0, crates[start-1].pop(0))
        moving = crates[start-1][0:num]
        crates[start-1] = crates[start-1][num::]
        for i in moving[::-1]:
            crates[end-1].insert(0, i)
        l = f.readline()

    return ''.join([c[0] for c in crates])
