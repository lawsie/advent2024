import re

with open("testinput.txt") as f:
    wordsearch = f.readlines()

wordsearch = [line.strip("\n") for line in wordsearch]


def across(wordsearch):
    total = 0

    for line in wordsearch:
        forwards = re.findall("XMAS", line)
        backwards = re.findall("SAMX", line)

        total += len(forwards) + len(backwards)

    return total


def updown(wordsearch):
    # Rotate the list so that the cols are now rows
    rotated = list(zip(*wordsearch[::1]))

    total = 0

    for line in rotated:
        str_line = "".join(line)
        forwards = re.findall("XMAS", str_line)
        backwards = re.findall("SAMX", str_line)

        total += len(forwards) + len(backwards)
    return total


def test_diagonal(search, row, col, direction, wordsearch):

    # Calculate bounds
    max_row = len(wordsearch)
    max_col = len(wordsearch[0])

    # If nothing else to search for, you must have found it
    if len(search) == 0:
        return 1
    else:
        new_r = row + direction[0]
        new_c = col + direction[1]

        # Check new position is in bounds
        if (0 < new_r < max_row) and (0 < new_c < max_col):

            # Check if this new location is the search letter
            if wordsearch[new_r][new_c] == search[0]:
                # print(f"Found {search[0]}")
                return test_diagonal(search[1:], new_r, new_c, direction, wordsearch)
            else:
                # print(f"Did not find {search[0]}, returning")
                return 0
        else:
            # print("Edge found, returning")
            return 0


def diagonal(wordsearch):
    total = 0
    for r in range(len(wordsearch)):
        for c in range(len(wordsearch[r])):
            if wordsearch[r][c] == "X":
                # print("Found an X")
                total += test_diagonal("MAS", r, c, [1, 1], wordsearch)
                total += test_diagonal("MAS", r, c, [-1, 1], wordsearch)
                total += test_diagonal("MAS", r, c, [1, -1], wordsearch)
                total += test_diagonal("MAS", r, c, [-1, -1], wordsearch)
    return total


print(f"{across(wordsearch)} across")
print(f"{updown(wordsearch)} up and down")
print(f"{diagonal(wordsearch)} diagonal")
