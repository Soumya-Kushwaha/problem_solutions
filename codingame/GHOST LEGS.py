W, H = map(int, input().split())

T = input().split("  ")
l = list(range(len(T)))

for _ in range(H - 2):
    line = input().split("|")

    for j in range(len(line)):
        if line[j] == "--":

            for k in range(len(l)):
                if l[k] == j - 1:
                    l[k] += 1
                elif l[k] == j:
                    l[k] -= 1

B = input().split("  ")

for i in range(len(T)):
    print(T[i] + B[l[i]])
