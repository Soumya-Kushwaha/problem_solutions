import math

lonA = float(input().replace(",", "."))
latA = float(input().replace(",", "."))
n = int(input())
res = []
for _ in range(n):
    defib = input().replace(",", ".").split(";")
    lonB, latB = float(defib[-2]), float(defib[-1])
    x = (lonB - lonA) * math.cos((latA + latB) / 2)
    y = latB - latA
    d = math.sqrt(x**2 + y**2) * 6371
    res += ((d, defib[1]),)
print(min(res)[1])
