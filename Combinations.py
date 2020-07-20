def _subcombinations(ls, r, rs, s=[]):
    for i in range(len(ls)):
        if len(s) + (len(ls)-i) < r: return #avoid any extra cycles
        s.append(ls[i])
        rs.append(''.join(s)) if len(s) == r else _subcombinations(ls[i+1:], r, rs, s)
        s.pop()

def combinations(s):
    rs = []
    l = list(s)
    for i in range(1,len(l)+1):
        _subcombinations(l,i,rs)
    return rs

if __name__ == "__main__":
    print(combinations('abc'))
