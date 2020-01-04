def divisors(n):
    """
    Create a function named divisors/Divisors that takes an integer n > 1 
    and returns an array with all of the integer's divisors
    (except for 1 and the number itself), from smallest to largest. 
    If the number is prime return the string '(integer) is prime' .
    Example:
    divisors(12); #should return [2,3,4,6]
    divisors(25); #should return [5]
    divisors(13); #should return "13 is prime"
    """
    lst = [i for i in range(2, n) if n % i == 0]
    if len(lst):
        return lst
    else:
        return '{} is prime'.format(n)

if __name__ == "__main__":
    print(divisors(12))
    print(divisors(25))
    print(divisors(13))