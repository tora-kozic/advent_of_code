
def lanternfish(f, days):
    lines = f.readlines()
    fish = lines[0].split(',')
    fish = [int(i) for i in fish]
    # set up stats array
    stats = [0] * 9
    for i in range(len(fish)):
        stats[fish[i]] += 1
    # run days
    for i in range(days):
        stats = quick_day(stats)
    return sum(stats)


def quick_day(stats):
    new_fish = stats[0]
    stats = stats[1:] + [stats[0]]
    stats[6] += new_fish
    return stats


# PART 1
def day(fishes):
    for i in range(len(fishes)):
        fish = fishes[i]
        if fish == 0:
            fishes[i] = 6
            fishes.append(8)
        else:
            fishes[i] -= 1
    return fishes


f = open("input.txt", "r")
d = 256
x = lanternfish(f, d)
print(f"AFTER {d} DAYS, THERE ARE {x} LANTERNFISH.")
f.close()