n = int(input())
D = {}
for _ in range(n):
    inputs = input().split()
    b = inputs[0]
    c = int(inputs[1])
    D[b] = chr(c)

s = input()
decode = ""
hanging = ""
ind = 0
for i in s:
    hanging += i
    if hanging in D:
        decode += D[hanging]
        ind += len(hanging)
        hanging = ""

print(f"DECODE FAIL AT INDEX {ind}" if hanging else decode)
