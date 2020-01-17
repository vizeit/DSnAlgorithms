def zeros(n):
    """
    Write a program that will calculate the number of trailing zeros in a factorial of a given number.

    N! = 1 * 2 * 3 * ... * N

    Be careful 1000! has 2568 digits...

    For more info, see: http://mathworld.wolfram.com/Factorial.html
    Examples

    zeros(6) = 1
    # 6! = 1 * 2 * 3 * 4 * 5 * 6 = 720 --> 1 trailing zero

    zeros(12) = 2
    # 12! = 479001600 --> 2 trailing zeros
    """
    ts = 0
    i = 1
    while n//5**i > 0:
        ts += n//5**i
        i += 1
    return ts

if __name__ == "__main__":
    print(zeros(12))
    print(zeros(1000))