def test(levels):

    # Check if increasing or decreasing
    decreasing = True
    if levels[0] < levels[1]:
        decreasing = False

    # The levels are either all increasing or all decreasing.
    for i in range(len(levels) - 1):
        if decreasing:
            if levels[i] < levels[i + 1]:
                return False
        else:
            if levels[i] > levels[i + 1]:
                return False
        # Any two adjacent levels differ by at least one and at most three.
        diff = max(levels[i], levels[i + 1]) - min(levels[i], levels[i + 1])
        if diff < 1 or diff > 3:
            return False
    return True


with open("input.txt") as f:
    report = f.readlines()

report = [r.strip("\n").split(" ") for r in report]

safe = 0

for line in report:
    line = [int(x) for x in line]
    if test(line):
        safe += 1

print(safe)
