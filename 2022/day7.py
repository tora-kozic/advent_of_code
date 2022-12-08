
SIZE_KEY = 'TOTAL'
MAX_SIZE = 100000
TOTAL_SPACE = 70000000
REQUIRED_SPACE = 30000000


def part_one(f):
    tree = {}
    dirs = {}
    cwd = []
    l = f.readline()
    while l:
        if '$' in l:
            if 'cd' in l:
                d = [x.strip() for x in l.split(' ')][-1]
                if d == '/':
                    cwd = []
                elif d == '..':
                    cwd.pop()
                else:
                    cwd.append(d)
                l = f.readline()
            elif 'ls' in l:
                l = f.readline()
                while '$' not in l and l:
                    v = [x.strip() for x in l.split(' ')]
                    if v[0] == 'dir':
                        set_item(tree, cwd, {v[1]: {}})
                        set_item(dirs, cwd, {v[1]: {}})
                    else:
                        set_item(dirs, cwd, {v[1]: int(v[0])})
                    l = f.readline()
        else:
            l = f.readline()
    sum_branches(tree, dirs)
    return find_dir_to_delete(tree)
    # return calc_score(tree)


def set_item(d, l, v):
    if not l:
        d.update(v)
        return
    if len(l) == 1:
        d[l[0]].update(v)
        return
    set_item(d[l[0]], l[1:], v)


def sum_branches(tree: dict, dirs: dict):
    tree[SIZE_KEY] = 0
    for k, v in dirs.items():
        if k == SIZE_KEY:
            return 0
        if isinstance(v, dict):
            tree[SIZE_KEY] += sum_branches(tree[k], dirs[k])
        else:
            tree[SIZE_KEY] += v
    return tree[SIZE_KEY]


def calc_score(tree):
    sum = 0
    if tree[SIZE_KEY] < MAX_SIZE:
        sum += tree[SIZE_KEY]
    for k,v in tree.items():
        if isinstance(v, dict):
            sum += calc_score(tree[k])
    return sum


def find_dir_to_delete(tree):
    needed_space = REQUIRED_SPACE - (TOTAL_SPACE - tree[SIZE_KEY])
    return helper(tree, [], needed_space)


def helper(tree, valid_dirs, needed_space):
    if tree[SIZE_KEY] > needed_space:
        valid_dirs.append(tree[SIZE_KEY])
    for k,v in tree.items():
        if isinstance(v, dict):
            helper(tree[k], valid_dirs, needed_space)
    return min(valid_dirs)
