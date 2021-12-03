file = open('file', 'r')
array = file.read().splitlines()
array = list(map(int, array))

lenght = len(array)
for i in range (0, lenght-2):
    for j in range(i+1, lenght-1):
        for k in array[j+1:]:
            if (array[i]+array[j]+k) == 2020:
                print(array[i]*array[j]*k)
file.close()