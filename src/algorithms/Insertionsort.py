def Insertionsort(l):
    """
    Insertion sort
    """
    i = 0
    while i+1 < len(l):
        j = i + 1
        while j and l[j-1] > l[j]:
            l[j-1], l[j] = l[j], l[j-1]
            j -= 1
        i += 1
    return l