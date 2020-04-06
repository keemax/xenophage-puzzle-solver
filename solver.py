# rough representation of symbols
# A = 0
# X = 1
# / = 2
# T = 3
from collections import deque

solution = 1
initial = [
    [2, 0, 3],
    [3, 1, 3],
    [2, 0, 3]
]
seen = set()


def top_left(puzzle):
    return [
        [(puzzle[0][0] + 1) % 4, (puzzle[0][1] + 1) % 4,  (puzzle[0][2] + 1) % 4],
        [(puzzle[1][0] + 1) % 4, puzzle[1][1], puzzle[1][2]],
        [(puzzle[2][0] + 1) % 4, puzzle[2][1], puzzle[2][2]]
    ]


def top_middle(puzzle):
    return [
        [(puzzle[0][0] + 1) % 4, (puzzle[0][1] + 1) % 4,  (puzzle[0][2] + 1) % 4],
        [puzzle[1][0], (puzzle[1][1] + 1) % 4, puzzle[1][2]],
        [puzzle[2][0], (puzzle[2][1] + 1) % 4, puzzle[2][2]]
    ]


def top_right(puzzle):
    return [
        [(puzzle[0][0] + 1) % 4, (puzzle[0][1] + 1) % 4,  (puzzle[0][2] + 1) % 4],
        [puzzle[1][0], puzzle[1][1], (puzzle[1][2] + 1) % 4],
        [puzzle[2][0], puzzle[2][1], (puzzle[2][2] + 1) % 4]
    ]


def middle_left(puzzle):
    return [
        [(puzzle[0][0] + 1) % 4, puzzle[0][1],  puzzle[0][2]],
        [(puzzle[1][0] + 1) % 4, (puzzle[1][1] + 1) % 4, (puzzle[1][2] + 1) % 4],
        [(puzzle[2][0] + 1) % 4, puzzle[2][1], puzzle[2][2]]
    ]


def middle(puzzle):
    return [
        [puzzle[0][0], (puzzle[0][1] + 1) % 4,  puzzle[0][2]],
        [(puzzle[1][0] + 1) % 4, (puzzle[1][1] + 1) % 4, (puzzle[1][2] + 1) % 4],
        [puzzle[2][0], (puzzle[2][1] + 1) % 4, puzzle[2][2]]
    ]


def middle_right(puzzle):
    return [
        [puzzle[0][0], puzzle[0][1],  (puzzle[0][2] + 1) % 4],
        [(puzzle[1][0] + 1) % 4, (puzzle[1][1] + 1) % 4, (puzzle[1][2] + 1) % 4],
        [puzzle[2][0], puzzle[2][1], (puzzle[2][2] + 1) % 4]
    ]


def bottom_left(puzzle):
    return [
        [(puzzle[0][0] + 1) % 4, puzzle[0][1],  puzzle[0][2]],
        [(puzzle[1][0] + 1) % 4, puzzle[1][1], puzzle[1][2]],
        [(puzzle[2][0] + 1) % 4, (puzzle[2][1] + 1) % 4, (puzzle[2][2] + 1) % 4]
    ]


def bottom_middle(puzzle):
    return [
        [puzzle[0][0], (puzzle[0][1] + 1) % 4,  puzzle[0][2]],
        [puzzle[1][0], (puzzle[1][1] + 1) % 4, puzzle[1][2]],
        [(puzzle[2][0] + 1) % 4, (puzzle[2][1] + 1) % 4, (puzzle[2][2] + 1) % 4]
    ]


def bottom_right(puzzle):
    return [
        [puzzle[0][0], puzzle[0][1],  (puzzle[0][2] + 1) % 4],
        [puzzle[1][0], puzzle[1][1], (puzzle[1][2] + 1) % 4],
        [(puzzle[2][0] + 1) % 4, (puzzle[2][1] + 1) % 4, (puzzle[2][2] + 1) % 4]
    ]


def is_solved(puzzle):
    for row in puzzle:
        for col in row:
            if col != solution:
                return False
    return True


def print_solution(t):
    moves = deque()
    while t is not None:
        moves.appendleft(t[1])
        t = t[2]
    # get rid of 'initial' from output
    moves.popleft()
    for move in moves:
        print(move)


def check_seen(puzzle):
    puzzle_str = ''.join([str(j) for i in puzzle for j in i])
    if puzzle_str in seen:
        return True
    seen.add(puzzle_str)
    return False


def main():
    puzzles = deque()
    puzzles.append((initial, 'initial', None))
    solved = False
    while not solved and len(puzzles) > 0:
        puzzle_tup = puzzles.popleft()
        p = puzzle_tup[0]
        if check_seen(p):
            continue
        if is_solved(p):
            print_solution(puzzle_tup)
            solved = True
        else:
            puzzles.append((top_left(p), 'top left', puzzle_tup))
            puzzles.append((top_middle(p), 'top middle', puzzle_tup))
            puzzles.append((top_right(p), 'top right', puzzle_tup))
            puzzles.append((middle_left(p), 'middle left', puzzle_tup))
            puzzles.append((middle(p), 'middle', puzzle_tup))
            puzzles.append((middle_right(p), 'middle right', puzzle_tup))
            puzzles.append((bottom_left(p), 'bottom left', puzzle_tup))
            puzzles.append((bottom_middle(p), 'bottom middle', puzzle_tup))
            puzzles.append((bottom_right(p), 'bottom right', puzzle_tup))
    if not solved:
        print('no solution')


if __name__ == "__main__":
    main()
