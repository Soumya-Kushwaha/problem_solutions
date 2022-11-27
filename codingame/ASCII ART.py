alp = "ABCDEFGHIJKLMNOPQRSTUVWXYZ?"
l = int(input())
h = int(input())
t = input().upper()
rows = []
for _ in range(h):
    row = input()
    rows.append(row)
for i in rows:
    for sym in t:
        fi = alp.find(sym)
        if fi == -1:
            fi = 26
        print(i[l * fi : l * (fi + 1)], end="")
    print()
