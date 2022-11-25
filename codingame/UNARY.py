import itertools

message = input()
s = "".join(
    "0" * (7 - len(bin(ord(i))[2:])) + bin(ord(i))[2:] for i in message
)

answer = ""
for char, char_counter in itertools.groupby(s):
    a = list(char_counter).copy()
    if a[0] == "1":
        answer += "0 " + ("0" * len(a)) + " "
    else:
        answer += "00 " + ("0" * len(a)) + " "
print(answer[:-1])
