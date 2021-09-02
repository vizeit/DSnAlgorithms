def _subcombinations(ls, r, s=[]):
    for i in range(len(ls)):
        if len(s) + (len(ls)-i) < r: break #avoid any extra cycles
        s.append(ls[i])
        if len(s) == r: 
            yield ''.join(s)
        else: 
            yield from _subcombinations(ls[i+1:], r, s)
        s.pop()

def combinations(s):
    l = list(s)
    for i in range(1,len(l)+1):
        yield from _subcombinations(l,i)

if __name__ == "__main__":
    for c in combinations('abc'):
        print(c, end=' ')
