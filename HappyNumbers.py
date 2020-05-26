from multiprocessing import Pool
import time

st = set()
sf = set()

def sqre(n):
    s = 0
    while n:
        n, d = divmod(n, 10)
        s += d**2
    return s

def ishappy(n):
    global st
    global sf

    s = []
    su = n
    while True:
        su = sqre(su)
        if su == 1 or su in st:
            if s:
                st.add(s[0])
            return n
        if su in s or su in sf:
            if s:
                sf.add(s[0])
            break
        s.append(su)

def performant_numbers(n):
    """
    Function returns list of Happy numbers between 1 to n
    """
    if n < 5000:
        return [i for i in range(n+1) if ishappy(i) is not None]
    rs = []
    with Pool(4) as p:
        for i in p.map(ishappy, range(n+1)):
            if i is not None:
                rs.append(i)
    return rs

if __name__ == "__main__":
    l = [
        59090,114742,104721,194554,15314,293211,198561,118033,243374,138837,73094,33641,105638,281895,52600,193311,214239,66672,188339,221677,87299,127372,74204
    ]
    start  = time.time()
    for i in l:
        performant_numbers(i)
    print(time.time() - start)
