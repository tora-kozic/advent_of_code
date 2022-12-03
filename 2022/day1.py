N_MAX = 2

f = open("day1/input.txt", "r")
lines = f.readlines()
max_cals = []
min_max = 0
elves = []
cals = 0
for l in lines:
    if l in ['', '\n']:
        elves.append(cals)
        if len(max_cals) < N_MAX:
            max_cals.append(cals)
        else:
            if cals > min_max:
                if min_max > 0:
                    max_cals.remove(min_max)
                max_cals.append(cals)
                min_max = min(max_cals)
        cals = 0
    else:
        cals += int(l.strip())

print(sum(max_cals))
f.close()
