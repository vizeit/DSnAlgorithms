def permutations(k, s, u, rs):
    for i, e in enumerate(u):
        s.append(u.pop(i))
        if k == 1:
            rs.append(''.join(s))
        else:
            permutations(k-1, s, u,rs)
        u.insert(i,s.pop())#backtracking

if __name__ == "__main__":
    rs = []
    s = 'abcd'
    permutations(len(s), [], list(s),rs)
    print(rs)