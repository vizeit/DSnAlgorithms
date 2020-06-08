def SelectionSort(l):
    """
    Selection Sort
    """
    for i in range(len(l)):
        minindex = i
        for j in range(i+1, len(l)):
            if l[j] < l[minindex]:
                minindex = j
        l[i], l[minindex] = l[minindex], l[i]

if __name__ == "__main__":
    import random
    rn = 500
    l = []
    for i in range(rn):
        l.append(random.randrange(rn))
    SelectionSort(l)
    print(l)