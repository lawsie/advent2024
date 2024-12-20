import re

with open("input.txt") as f:
    report = f.read()

# Filter out anything marked don't
all_dos = re.split(r"do\(\)", report)

# Keep a total
total = 0

for do in all_dos:
    # Throw out everything after don't
    stop_at = re.split(r"don't\(\)", do)

    # Use regex to find the instructions in the bit prior
    instructions = re.findall(r"mul\([0-9]+,[0-9]+\)", stop_at[0])

    # Do the multiplication
    for i in instructions:
        result = i.strip("mul()").split(",")
        total += int(result[0]) * int(result[1])

print(total)
