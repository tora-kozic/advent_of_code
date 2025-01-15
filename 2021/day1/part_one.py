
f = open("input.txt", "r")
count = 0
init_pos = f.tell()
last_num = int(f.readline())
f.seek(init_pos)
for x in f:
    if int(x) > last_num:
        count += 1
    last_num = int(x)
f.close()
print(count)
