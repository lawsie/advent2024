import re

with open("input.txt") as f:
    report = f.read()

# Use regex to find the instructions
instructions = re.findall("mul\([0-9]+,[0-9]+\)", report)

# Do the multiplication
total = 0
for i in instructions:
    result = i.strip("mul()").split(",")
    total += int(result[0]) * int(result[1])

print(total)
