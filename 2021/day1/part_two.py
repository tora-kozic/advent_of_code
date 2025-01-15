
# Take some window n, for every sum of n numbers from file f, compare the sums.
# Return the number of times the sum increases from the previous
def window(f, n):
    lines = f.readlines()
    first_idx = 0
    second_idx = n
    count = 0
    while second_idx < len(lines):
        first = int(lines[first_idx])
        second = int(lines[second_idx])
        if second > first:
            count += 1
        first_idx += 1
        second_idx += 1
    return count


f = open("input.txt", "r")
n = 3
print(window(f, n))
