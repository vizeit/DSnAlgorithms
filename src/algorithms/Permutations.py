def _subpermutations(u, r, s=[]):
    for i in range(len(u)):
        s.append(u.pop(i))
        if r == 1: 
            yield ''.join(s)
        else: 
            yield from _subpermutations(u, r-1, s)
        u.insert(i,s.pop())#backtracking

def Permutations(s):
    l = list(s)
    for i in range(1, len(l)+1):
        yield from _subpermutations(l, i)