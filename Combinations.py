def _subcombinations(ls, r, s=[]):
    for i in range(len(ls)):
        s.append(ls[i])
        if len(s) == r: yield ''.join(s) 
        yield from _subcombinations(ls[i+1:], r, s)
        s.pop()

def combinations(s):
    l = list(s)
    for i in range(1,len(l)+1):
        yield from _subcombinations(l,i)

if __name__ == "__main__":
    for c in combinations('abc'):
        print(c, end=' ')
