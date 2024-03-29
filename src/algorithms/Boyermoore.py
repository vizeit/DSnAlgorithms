def Boyermoore(str, p):
    """
    Boyer-Moore algorithm to match the pattern 'p' in 
    the string _string
    return the index of the starting position in _string
    or -1 if pattern is not found in the text
    """
    n = len(str) #length of the string
    m = len(p) #length of the pattern string
    if n == 0 or m == 0:
        return -1 #base scenario
    #create jump dictionary for mismatch scenario
    jump = {}
    for c in range(m):
        jump[p[c]] = c
    i = m - 1
    k = m - 1
    while i < n:
        if str[i] == p[k]:
            if k == 0:
                return i
            else:
                k -= 1
                i -= 1
        else:
            j = jump.get(str[i], -1) #-1 if not found
            i += m - min(k, j+1) #k is at index less than j, jump m-k. otherwise at m - j+1
            k = m - 1 #initialize k back to m-1
    return -1

