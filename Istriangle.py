def is_triangle(a, b, c):
    """
    Implement a method that accepts 3 integer values a, b, c. 
    The method should return true if a triangle can be built with 
    the sides of given length and false in any other case.
    (In this case, all triangles must have surface greater than 0 
    to be accepted).
    """
    ls = sorted([a,b,c])
    return ls[0] + ls[1] > ls[2]

if __name__ == "__main__":
    print(is_triangle(1,2,3))
    print(is_triangle(1,1,2))
    print(is_triangle(2,3,2))