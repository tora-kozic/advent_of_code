

def low_points(f):
    pts = []
    lines = f.readlines()
    lines = [list(s.strip()) for s in lines]
    for i in range(len(lines)):
        lines[i] = [int(x) for x in lines[i]]
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            pt = helper(lines, i, j)
            if pt == -1:
                continue
            if pt not in pts:
                pts.append(pt)
    basins = []
    for x in pts:
        basin = basin_helper(lines, x[0], x[1], 0)
        #print(f"BASIN ~ {basin}")
        basins.append(basin)
    basins.sort()
    return basins[-1] * basins[-2] * basins[-3]


def helper(arr, x, y):
    adj = edge_cases(arr, x, y)
    for k in adj.keys():
        i, j = k
        adj[k] = arr[i][j]

    # check if all values are the same (ie. there is no low point)
    all_same = True
    val = list(adj.values())[0]
    for v in adj.values():
        if v != val:
            all_same = False
            break
    if all_same:
        return -1
    if min(adj.values()) == adj[(x, y)]:
        return x, y
    min_key = min(adj, key=adj.get)
    return helper(arr, min_key[0], min_key[1])


def edge_cases(arr, x, y):
    adj = {(x, y): 10, (x - 1, y): 10, (x + 1, y): 10, (x, y + 1): 10, (x, y - 1): 10}
    # top edge case
    if x == 0:
        adj.pop((x - 1, y))
    # bottom edge case
    if x == len(arr) - 1:
        adj.pop((x + 1, y))
    # left edge case
    if y == 0:
        adj.pop((x, y - 1))
    # right edge case
    if y == len(arr[0]) - 1:
        adj.pop((x, y + 1))
    return adj


def basin_helper(arr, x, y, n):
    stop = [-1, 9]
    if arr[x][y] in stop:
        return 0
    adj = edge_cases(arr, x, y)
    adj.pop(x,y)
    _sum = 0
    for k in adj.keys():
        i, j = k
        arr[x][y] = -1
        _sum += basin_helper(arr, i, j, n+1)
    #print(f"ARR {x}, {y}: {arr[x][y]} ~ RETURN {_sum}")
    return 1 + _sum


f = open("input.txt", "r")
p = low_points(f)
print(p)
f.close()
