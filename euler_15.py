from utils import timer


@timer
def euler_15() -> int:
    grid = [[0] * 21 for _ in range(21)]
    for p in range(21):
        grid[p][0] = 1
        grid[0][p] = 1
    for r in range(1, 21):
        for c in range(1, 21):
            grid[r][c] = grid[r - 1][c] + grid[r][c - 1]
    print(grid[2][2])
    return grid[-1][-1]


if __name__ == "__main__":
    print(euler_15())
