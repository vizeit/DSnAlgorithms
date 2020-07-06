def _subpermutations(k, s, u, rs):
    for i, e in enumerate(u):
        s.append(u.pop(i))
        if k == 1:
            rs.append(''.join(s))
        else:
            _subpermutations(k-1, s, u,rs)
        u.insert(i,s.pop())#backtracking

def permutations(s):
    rs = []
    _subpermutations(len(s), [], list(s),rs)
    return rs

if __name__ == "__main__":
    print(permutations('abc'))
    