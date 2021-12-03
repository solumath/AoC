def problem1(data):
    x = 0
    for i in range(1, len(data)):
        if data[i] > data[i - 1]:
            x += 1
    print(x)

def problem2(data):
    x = 0
    for i in range(3, len(data)):
        if (data[i] + data[i - 1] + data[i - 2]) > (data[i - 1] + data[i - 2] + data[i - 3]):
            x += 1
    print(x)

if __name__ == '__main__':
    with open("data") as file:
        data = [int(line.strip()) for line in file]
    problem1(data)
    problem2(data)