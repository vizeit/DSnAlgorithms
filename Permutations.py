def _subpermutations(u, r, rs, s=[]):
    for i in range(len(u)):
        s.append(u.pop(i))
        rs.append(''.join(s)) if r == 1 else _subpermutations(u, r-1, rs, s)
        u.insert(i,s.pop())#backtracking

def permutations(s):
    rs = []
    l = list(s)
    for i in range(1, len(l)+1):
        _subpermutations(l, i, rs)
    return rs

if __name__ == "__main__":
    print(permutations('abc'))
    