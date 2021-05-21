file = open('passwords', 'r')
array = file.read().splitlines()
success = 0

#Part One
for item in array:
    elem = item.split()
    num = elem[0].split("-")
    char = elem[1][:1]
    passw = elem[2]
    times = passw.count(char)
    if int(num[0]) <= times <= int(num[1]):
        success += 1

print(f"Part One: {success}")
success = 0

# Part Two
for item in array:
    elem = item.split()
    num = elem[0].split("-")
    char = elem[1][:1]
    passw = elem[2]

    #indexing starts at 0
    index_1 = int(num[0]) - 1
    index_2 = int(num[1]) - 1
    
    # XOR is possible between 2 bools
    if bool(passw[index_1]==char) != bool(passw[index_2]==char):
        success += 1

file.close()
print(f"Part Two: {success}")