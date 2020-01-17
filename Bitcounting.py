def countBits(n):
    """
    Write a function that takes an integer as input, and 
    returns the number of bits that are equal to one in 
    the binary representation of that number. 
    You can guarantee that input is non-negative.
    Example: The binary representation of 1234 is 10011010010, 
    so the function should return 5 in this case
    """
    return '{0:b}'.format(n).count('1')

if __name__ == "__main__":
    print(countBits(1234))