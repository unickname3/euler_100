from utils import timer

TRIANGLE_FILENAME = "0067_triangle.txt"


@timer
def euler_18() -> int:
    with open(TRIANGLE_FILENAME, "r") as f:
        triangle_text = f.read()
    triangle = [
        list(map(int, line.split())) for line in triangle_text.strip().split("\n")
    ]
    print(triangle)
    last_line = triangle[0]
    for line in triangle[1:]:
        new_line = []
        for i in range(len(line)):
            if i == 0:
                new_line.append(last_line[0] + line[0])
            elif i == len(line) - 1:
                new_line.append(last_line[i - 1] + line[i])
            else:
                new_line.append(max(last_line[i - 1], last_line[i]) + line[i])
        last_line = new_line
    return max(last_line)


if __name__ == "__main__":
    print(euler_18())
