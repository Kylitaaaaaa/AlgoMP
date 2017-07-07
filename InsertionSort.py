# a = [35, 2, 9, 0, 67]

def insertionSort(list):
    print(list)
    for x in range(1, len(list)):
        curr = list[x]
        for y in range(x, 0, -1):

            if list[y-1] > curr:
                list[y] = list[y-1]
                list[y-1] = curr
            print(list, ", ", x)



a = []

in1 = "go"

while in1 != -1:
    in1 = input('enter number: ')
    if in1 != -1:
        a.append(in1)
    else:
        print(a)

insertionSort(a)