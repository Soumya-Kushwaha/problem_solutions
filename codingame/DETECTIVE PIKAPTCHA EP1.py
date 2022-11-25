width, height = [int(i) for i in input().split()]
maps = []
for i in range(height):
    line = input()
    maps += (list(line),)

for y, i in enumerate(maps):
    for x, j in enumerate(i):
        if j == "#":
            continue
        count = 0
        if y >= 1:
            count += maps[y - 1][x] != "#"
        if x >= 1:
            count += maps[y][x - 1] != "#"
        if y + 1 < height:
            count += maps[y + 1][x] != "#"
        if x + 1 < width:
            count += maps[y][x + 1] != "#"
        maps[y][x] = str(count)

for i in maps:
    print("".join(i))
