def InsertionSort(l):
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

if __name__ == "__main__":
    print(InsertionSort([2, 8, 5, 3, 9, 4, 1, 7, 34, 343535, 54353, 676]))