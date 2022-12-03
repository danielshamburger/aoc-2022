def part_1():
    input = open("i.txt", "r").read()
    lines = input.splitlines()
    score = 0

    for line in lines:
        print(line)
        comp1 = slice(0, len(line)//2)
        comp2 = slice(len(line)//2, len(line))

        in_both = ""

        for char in line[comp1]:
            if char in line[comp2] and char not in in_both:
                in_both += char

        for c in in_both:
            if c.isupper():
                score += ord(c) - 38
            else:
                score += ord(c) - 96
                
    return score


def part_2():
    input = open("i.txt", "r").read()
    lines = input.splitlines()
    score = 0

    i = 0
    while i < len(lines):
        in_both = ""
        for c in lines[i]:
            if c in lines[i+1] and c in lines[i+2] and c not in in_both:
                in_both += c
        
        for c in in_both:
            if c.isupper():
                score += ord(c) - 38
            else:
                score += ord(c) - 96

        i += 3

    return score
        

def main():
    print(part_1())
    print(part_2())



main()