def MergeSort(l):
    """
    Merge Sort
    """
    if len(l) <= 1:
        return l

    ll = MergeSort(l[:len(l)//2])
    lr = MergeSort(l[len(l)//2:])
    return Merge(ll, lr)

def Merge(ll, lr):
    l = []
    i = j = 0
    while i < len(ll) or j < len(lr):
        if i == len(ll):
            l.append(lr[j])
            j += 1
        elif j == len(lr):
            l.append(ll[i])
            i += 1
        elif ll[i] < lr[j]:
            l.append(ll[i])
            i += 1
        else:
            l.append(lr[j])
            j += 1
    return l

if __name__ == "__main__":
    import random
    rn = 500
    l = []
    for i in range(rn):
        l.append(random.randrange(rn))
    print(MergeSort(l))