with open("input.txt") as f:
    loc = f.readlines()

# Make a list of lists from each line
newlist = [item.strip("\n").split("  ") for item in loc]

# Unzip them into 2 lists
first, second = list(zip(*newlist))

# Sort and convert to int
first = sorted([int(num) for num in first])
second = sorted([int(num) for num in second])

total = 0
for i in range(len(first)):
    total += max(first[i], second[i]) - min(first[i], second[i])

print(total)
