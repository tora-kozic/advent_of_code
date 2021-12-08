def bingo(f):
    # read file
    lines = f.readlines()
    # take first line and comma split to find numbers called
    input = lines[0].split(',')
    # split into list of boards
    boards = []
    for i in range(len(lines)):
        if lines[i] == "\n" and lines[i+1] != "\n":
            board = []
            # each board is 5x5
            for j in range(5):
                board.append(lines[i+1+j])
                board[j] = board[j].split()
            boards.append(board)
    # store which board wins when and with what score
    winning_boards = [0] * len(boards)
    win_order = 1
    # for each number called
    for i in input:
        # for each board
        for j in range(len(boards)):
            board = boards[j]
            # replace called numbers with x
            board = replace(board, i)
            # check if board winner
            if check_board(board) and winning_boards[j] == 0:
                # if yes, return score
                winning_boards[j] = (calc_score(board) * int(i), win_order)
                win_order += 1
    return winning_boards


def check_board(b):
    for i in range(len(b)):
        # check if winner in rows
        if b[i][0] == 'X':
            for j in range(len(b[i])):
                if b[i][j] != 'X':
                    break
                if j == 4:
                    return True
        # check if winner in columns
        if b[0][i] == 'X':
            for j in range(len(b[i])):
                if b[j][i] != 'X':
                    break
                if j == 4:
                    return True
    return False


def replace(b, x):
    for i in range(len(b)):
        for j in range(len(b[i])):
            if b[i][j] == x:
                b[i][j] = 'X'
                return b
    return b


# calculate board score
def calc_score(b):
    _sum = 0
    # return sum of unchecked numbers
    for i in range(len(b)):
        for j in range(len(b[i])):
            try:
                _sum += int(b[i][j])
            except ValueError:
                continue
    return _sum

f = open("input.txt", "r")
wins = bingo(f)
print(len(wins))
for x in range(len(wins)):
    s, order = wins[x]
    print(f"BOARD {x} won in {order}-PLACE with a SCORE of {s}")
