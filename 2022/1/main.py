def problem1(elfs):
    max = 0
    for elf in elfs:
        max = sum(elf) if max < sum(elf) else max
    print(max)

def problem2(elfs):
    sums = [sum(elf) for elf in elfs]
    sums.sort(reverse=True)
    print(sum(sums[:3]))

if __name__ == '__main__':
    with open("data", "r") as file:
        elfs = [list(map(int, elf.split("\n"))) for elf in file.read().split("\n\n")]
    problem1(elfs)
    problem2(elfs)
