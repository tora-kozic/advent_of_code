
LOSE = 0
DRAW = 3
WIN = 6


def part_one(lines):
    shape_score = ["X", "Y", "Z"]  # score is index + 1
    matchup = {
        "A": {"X": DRAW, "Y": WIN},
        "B": {"Y": DRAW, "Z": WIN},
        "C": {"Z": DRAW, "X": WIN}
    }

    def score_line(line):
        l = [l.strip() for l in line.split(" ")]
        s = shape_score.index(l[1]) + 1
        try:
            return s + matchup[l[0]][l[1]]
        except KeyError:
            return s + LOSE

    scores = [score_line(l) for l in lines]

    return sum(scores)


def part_two(lines):
    shape = {
        "X": LOSE,
        "Y": DRAW,
        "Z": WIN
    }
    matchup = {
        "A": {"Y": 1, "Z": 2, "X": 3},
        "B": {"Y": 2, "Z": 3, "X": 1},
        "C": {"Y": 3, "Z": 1, "X": 2}
    }

    def score_line(line):
        l = [l.strip() for l in line.split(" ")]
        s = shape[l[1]]
        return s + matchup[l[0]][l[1]]

    scores = [score_line(l) for l in lines]

    return sum(scores)


f = open("input.txt", "r")
lines = f.readlines()
print(f"PART ONE: {part_one(lines)}")
print(f"PART TWO: {part_two(lines)}")
f.close()
