import numpy

w = int(input())
h = int(input())
m = []
for _ in range(h):
    line = input()
    m += ([*line],)

m = numpy.array(m)
k = m.copy()
for y in range(h):
    miny = max(y - 1, 0)
    maxy = min(y + 2, h)
    for x in range(w):
        minx = max(x - 1, 0)
        maxx = min(x + 2, w)
        grid = m[miny:maxy, minx:maxx]
        char = m[y][x]
        if char == "x":
            k[y][x] = "."
        else:
            k[y][x] = sum(map(lambda x: [*x].count("x"), grid)) or "."

for i in k:
    print(*i, sep="")
