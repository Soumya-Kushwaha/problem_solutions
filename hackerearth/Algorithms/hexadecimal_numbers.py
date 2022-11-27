import math
for _ in range(int(input())):
    a,b = map(int, input().split())
    print(sum(math.gcd(sum(map(lambda x:int(x, 16), f'{f:x}')),f) > 1 for f in range(a, b + 1)))