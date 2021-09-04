def partition(l, lo, hi):
    p = l[lo]
    i = lo
    j = hi+1
    while 1:
        i += 1
        while l[i] < p and l[i] != p:
            if i == hi:
                break
            i += 1
        j -= 1
        while l[j] > p and l[j] != p:
            if j == lo:
                break
            j -= 1
        if i >= j:
            break
        l[i], l[j] = l[j], l[i]
    l[lo], l[j] = l[j], p
    return j


def _quicksort(l, lo, hi):
    if hi <= lo:
        return
    ip = partition(l, lo, hi)

    _quicksort(l, lo, ip-1)
    _quicksort(l, ip+1, hi)

def Quicksort(l):
    _quicksort(l, 0, len(l)-1)
    