from re import sub

text = input().lower()
space_fix = sub(r"([\w])\s+([\s,.!?\\-]+)", r"\1\2", text)
punctuation_fix = sub(r"([\s,.!?\\-]+)", lambda match: match.group(1)[0], space_fix)
one_space = sub(r"(\W)\s*(.)", r"\1 \2", punctuation_fix)
no_spaces = sub(r"\s+([\W])", r"\1", one_space)
capitalize = sub(
    r"(^[a-z]|\. [a-z])", lambda match: f"{match.group(1).upper()}", no_spaces
)

print(capitalize)
