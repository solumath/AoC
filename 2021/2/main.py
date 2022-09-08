def problem1(data):
    depth = 0
    pos = 0
    for order in data:
        direction = order.split(" ")[0]
        value = int(order.split(" ")[1])
        if direction == "forward":
            pos += value
        if direction == "up":
            depth -= value
        if direction == "down":
            depth += value

    print(depth*pos)

def problem2(data):
    depth = 0
    pos = 0
    aim = 0
    for order in data:
        direction = order.split(" ")[0]
        value = int(order.split(" ")[1])
        if direction == "forward":
            pos += value
            depth += value*aim
        if direction == "up":
            aim -= value
        if direction == "down":
            aim += value

    print(depth*pos)

if __name__ == '__main__':
    with open("data") as file:
        data = [str(line.strip()) for line in file]
    problem1(data)
    problem2(data)