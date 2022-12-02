def part_1():
    input = open("i.txt", "r").read()
    games = input.splitlines()
    
    scores = []

    rock = 'X'
    paper = 'Y'
    scissors = 'Z'

    Rock = 'A'
    Paper = 'B'
    Scissors = 'C'

    for game in games:
        shape_score = 0
        win = False
        draw = False

        if game[-1] == rock:
            shape_score = 1
            if game[0] == Scissors:
                win = True
            if game[0] == Rock:
                draw = True

        if game[-1] == paper:
            shape_score = 2
            if game[0] == Rock:
                win = True
            if game[0] == Paper:
                draw = True

        if game[-1] == scissors:
            shape_score = 3
            if game[0] == Paper:
                win = True
            if game[0] == Scissors:
                draw = True

        if win:
            score = 6 + shape_score
        elif draw:
            score = 3 + shape_score
        else: 
            score = shape_score

        scores.append(score)

    return sum(scores)


def part_2():
    input = open("i.txt", "r").read()
    games = input.splitlines()
    
    scores = []

    rock = 'A'
    paper = 'B'
    scissors = 'C'

    lose = 'X'
    draw = 'Y'
    win = 'Z'

    for game in games:
        shape_score = 0
        ending = 'lose'
        play = 'rock'

        opponent = game[0]
        strategy = game[-1]

        if strategy == lose:
            if opponent == rock:
                play = scissors
            if opponent == paper:
                play = rock
            if opponent == scissors:
                play = paper
        elif strategy == draw:
            ending = 'draw'
            if opponent == rock:
                play = rock
            if opponent == paper:
                play = paper
            if opponent == scissors:
                play = scissors
        else:
            ending = 'win'
            if opponent == rock:
                play = paper
            if opponent == paper:
                play = scissors
            if opponent == scissors:
                play = rock

        if play == rock:
            shape_score = 1
        elif play == paper:
            shape_score = 2
        else: 
            shape_score = 3

        if ending == 'win':
            score = 6 + shape_score
        elif ending == 'draw':
            score = 3 + shape_score
        else: 
            score = shape_score

        scores.append(score)

    return sum(scores)


def main():
    print(part_1())
    print(part_2())


main()