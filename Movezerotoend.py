def move_zeros(array):
    """
    Write an algorithm that takes an array and moves all of 
    the zeros to the end, preserving the order of the other elements.
    move_zeros([false,1,0,1,2,0,1,3,"a"]) # returns[false,1,1,2,1,3,"a",0,0]
    """
    a1, a2 = [], []
    for e in array:
        if type(e) in [int, float] and e == 0:
            a2.append(e)
        else:
            a1.append(e)
    return a1+a2

if __name__ == "__main__":
    print(move_zeros([False,1,0,1,2,0,1,3,"a"]))