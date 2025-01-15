
DISTINCT_CHARS = 14

def part_one(f):
    content = f.readlines()[0]
    chars = []
    chars.extend(content[0:14])
    check_unique(chars)
    for i in range(4, len(content)):
        if check_unique(chars):
            return i
        chars.pop(0)
        chars.append(content[i])


def check_unique(chars):
    for i in range(len(chars)-1):
        for j in range(i+1, len(chars)):
            if chars[i] == chars[j]:
                return False
    return True
