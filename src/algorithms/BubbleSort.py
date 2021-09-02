def BubbleSort(l):
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

if __name__ == "__main__":
    import random
    rn = 500
    l = []
    for i in range(rn):
        l.append(random.randrange(rn))
    BubbleSort(l)
    print(l)