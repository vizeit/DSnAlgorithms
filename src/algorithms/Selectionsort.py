def Selectionsort(l):
    """
    Selection Sort
    """
    for i in range(len(l)-1):
        minindex = i
        for j in range(i+1, len(l)):
            if l[j] < l[minindex]:
                minindex = j
        l[i], l[minindex] = l[minindex], l[i]