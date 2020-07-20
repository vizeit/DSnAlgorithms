def combinations(ls, r, rs, s=[]):
    for i in range(len(ls)):
        if len(s) + (len(ls)-i) < r:#avoid any extra cycles
            return
        s.append(ls[i])
        if len(s) == r:
            rs.append(''.join(s))
            s.pop()
        else:
            combinations(ls[i+1:], r, rs, s)
            s.pop()

if __name__ == "__main__":
    rs = []
    l = list('abcde')
    for i in range(1,len(l)+1):
        combinations(l,i,rs)
    print(rs)
