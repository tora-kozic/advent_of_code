
def build_diagram(f):
    # read in lines
    hits = {}
    lines = read_in_data(f)
    for points in lines:
        first = points[0]
        second = points[1]
        slope_x = second[0] - first[0]
        slope_y = second[1] - first[1]
        slope = slope_y / slope_x if slope_x != 0 else slope_y
        x = first[0]
        y = first[1]
        while x <= second[0]:
            toggle = 1 if slope >= 0 else -1
            if slope_x == 0:
                for _ in range(int(slope) * toggle + 1):
                    hits = check_hits(x, y, hits)
                    y += 1 * toggle
            else:
                hits = check_hits(x, y, hits)
                y += int(slope)
            x += 1
    score = calc_score(hits)
    print(hits)
    return score


def check_hits(x, y, hits):
    hit_pt = (x, y)
    if hit_pt in hits:
        hits[hit_pt] += 1
    else:
        hits[hit_pt] = 1
    return hits


def read_in_data(f):
    lines = []
    for l in f:
        line = l.split('->')
        for i in range(len(line)):
            x, y = line[i].split(',')
            line[i] = (int(x), int(y))
        # only concern with horiz & vert lines
        if line[0][0] > line[1][0]:
            line[0], line[1] = line[1], line[0]
        # if line[0][0] == line[1][0] or line[0][1] == line[1][1]:
        lines.append(line)
    return lines


def calc_score(d):
    score = 0
    for v in d.values():
        if v >= 2:
            score += 1
    return score


f = open("input.txt", "r")
s = build_diagram(f)
print(s)
f.close()
