def count_sort(data1, data2):
    help = [0] * 26
    for i in range(len(data1)):
        index = ord(data1[i]) - ord('a')
        help[index] += 1
    print(help)
    for i in range(1, 26):
        help[i] += help[i-1]
    for i in range(len(data1)-1, -1, -1):
        index = ord(data1[i]) - ord('a')
        pos = help[index] - 1
        data2 = list(data2)
        data2[pos] = data1[i]
        help[index] -= 1
    print(data2)
    print(help)
data1 = "lincai"
data2 = "lsjfge"
count_sort(data1, data2)