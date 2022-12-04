def main():
    pairs = open("i.txt", "r").read().split("\n")
    subsets = 0
    overlap = 0

    for pair in pairs:
        assignments = pair.split(",")
        full_assignments = []

        for assignment_range in assignments:
            limits = assignment_range.split("-")

            assignment = range(int(limits[0]), int(limits[1]) + 1)

            full_assignments.append(assignment)

        if set(full_assignments[0]).issubset(set(full_assignments[1])) \
            or set(full_assignments[1]).issubset(set(full_assignments[0])):
            subsets += 1
        
        if any(section in full_assignments[1] for section in full_assignments[0]):
            overlap += 1

    print("Part 1: %s" %(subsets))
    print("Part 2: %s" %(overlap))



    return

main()
