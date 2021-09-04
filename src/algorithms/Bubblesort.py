def Bubblesort(l):
    """
    Bubble Sort
    """
    for i in range(len(l)):
        swap = False
        for j in range(len(l)-i-1):
            if l[j+1] < l[j]:
                l[j], l[j+1] = l[j+1], l[j]
                swap = True
        if not swap:
            break