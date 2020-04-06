# rough representation of symbols
# A = 0
# X = 1
# / = 2
# T = 3
import copy
from collections import deque

solution = 1
initial = [
    [2, 0, 3],
    [3, 1, 3],
    [2, 0, 3]
]
seen = set()


def new_state(old_state, row, col):
    state = copy.deepcopy(old_state)
    for i in range(len(state[row])):
        state[row][i] = (state[row][i] + 1) % 4
    for i in range(len(state)):
        if i != row:
            state[i][col] = (state[i][col] + 1) % 4
    return state


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
            puzzles.append((new_state(p, 0, 0), 'top left', puzzle_tup))
            puzzles.append((new_state(p, 0, 1), 'top middle', puzzle_tup))
            puzzles.append((new_state(p, 0, 2), 'top right', puzzle_tup))
            puzzles.append((new_state(p, 1, 0), 'middle left', puzzle_tup))
            puzzles.append((new_state(p, 1, 1), 'middle', puzzle_tup))
            puzzles.append((new_state(p, 1, 2), 'middle right', puzzle_tup))
            puzzles.append((new_state(p, 2, 0), 'bottom left', puzzle_tup))
            puzzles.append((new_state(p, 2, 1), 'bottom middle', puzzle_tup))
            puzzles.append((new_state(p, 2, 2), 'bottom right', puzzle_tup))
    if not solved:
        print('no solution')


if __name__ == "__main__":
    main()
