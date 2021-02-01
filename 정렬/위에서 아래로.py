n = int(input())
array = []

for i in range(n):
    m = int(input())
    array.append(m)

array = sorted(array, reverse=True)

for i in array:
    print(i)


