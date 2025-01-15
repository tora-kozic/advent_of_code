
# ()
# []
# <>
# {}

def syntax(f):
    lines = f.readlines()
    lines = [line.split() for line in lines]
    characters = []
    #table = {')': 3, ']': 57, '}': 1197, '>': 25137}
    table = {')': 1, ']': 2, '}': 3, '>': 4}
    for line in lines:
        c = check_corrupt(line[0])
        if c in table.keys():
            #characters.append(check_corrupt(line[0]))
            continue
        characters.append(check_incomplete(line[0]))
    #score = sum([table[c] for c in characters])
    score = []
    s = 0
    for line in characters:
        for i in range(len(line)):
            s *= 5
            s += table[line[i]]
        score.append(s)
        s = 0
    score.sort()
    l = len(score)
    idx = (len(score) - 1) // 2
    if l % 2 != 0:
        return score[idx]
    else:
        return (score[idx] + score[idx + 1]) / 2.0
    return score


def check_corrupt(line):
    x = ['(', '[', '{', '<']
    y = {')': '(', ']': '[', '}': '{', '>': '<'}  # maps closing brackets to open brackets
    last_open = []
    for i in range(len(line)):
        c = line[i]
        if c in x:
            last_open.append(c)
        else:  # if c in y.keys()
            if y[c] != last_open[-1]:
                return c
            else:
                last_open.pop()
    return 'X'


def check_incomplete(line):
    x = {'(': ')', '[': ']', '{': '}', '<': '>'}
    y = {')': '(', ']': '[', '}': '{', '>': '<'}  # maps closing brackets to open brackets
    last_open = []
    for i in range(len(line)):
        c = line[i]
        if c in x:
            last_open.append(c)
        else:
            last_open.pop()
    solve = ''
    while last_open:
        solve += x[last_open.pop()]
    return solve


f = open("input.txt", "r")
p = syntax(f)
print(p)
f.close()
