def problem1(rounds):
    score = 0
    points = {
        ("A", "X"): 4,
        ("A", "Y"): 8,
        ("A", "Z"): 3,
        ("B", "X"): 1,
        ("B", "Y"): 5,
        ("B", "Z"): 9,
        ("C", "X"): 7,
        ("C", "Y"): 2,
        ("C", "Z"): 6
    }
    for round in rounds:
        score += points[round]
    print(score)


def problem2(rounds):
    score = 0
    points = {
        ("A", "X"): 3,
        ("A", "Y"): 4,
        ("A", "Z"): 8,
        ("B", "X"): 1,
        ("B", "Y"): 5,
        ("B", "Z"): 9,
        ("C", "X"): 2,
        ("C", "Y"): 6,
        ("C", "Z"): 7
    }
    for round in rounds:
        score += points[round]
    print(score)

if __name__ == '__main__':
    with open("data", "r") as file:
        rounds = [(char[0], char[2]) for char in file.readlines()]
    problem1(rounds)
    problem2(rounds)
