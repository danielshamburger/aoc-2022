def part_1():
    input = open("input.txt", "r").read()
    lines = input.splitlines()
    
    totals = []
    calorie_tally = 0

    for i, line in enumerate(lines):
        if len(line) > 1:
            calorie_tally += int(line)
        else:
            totals.append(calorie_tally)
            calorie_tally = 0
        if i == len(lines) - 1:
            totals.append(calorie_tally)

    return max(totals)


def part_2():
    input = open("input.txt", "r").read()
    lines = input.splitlines()
    
    totals = []
    calorie_tally = 0

    for i, line in enumerate(lines):
        if len(line) > 1:
            calorie_tally += int(line)
        else:
            totals.append(calorie_tally)
            calorie_tally = 0
        if i == len(lines) - 1:
            totals.append(calorie_tally)


    first = max(totals)
    totals.remove(first)

    second = max(totals)
    totals.remove(second)

    third = max(totals)
    totals.remove(third)

    return first + second + third


def main():
    print(part_1())
    print(part_2())

main()