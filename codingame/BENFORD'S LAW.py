import re

b = [0, 30.1, 17.6, 12.5, 9.7, 7.9, 6.7, 5.8, 5.1, 4.6]
v = {}
regex = re.compile(r"x*([1-9]).*")

n = int(input())
for _ in range(n):
    nmb = int(re.search(regex, input())[1])
    v[nmb] = v.setdefault(nmb, 0) + 1
print(
    "false"
    if all(b[i] - 10 < v[i] / n * 100 < b[i] + 10 for i in v)
    else "true"
)
