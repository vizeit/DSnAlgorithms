def _atoi(s):
    """ 
    If you were asked to write your own atoi instead of using 
    native atoi() provided by Python
    return ascii to integer value 
    """
    return sum(( ord(c) - 48) * 10**i for i, c in enumerate(reversed(s)))

if __name__ == "__main__":
    print(_atoi('1234'))
    print(_atoi('4737357835839'))
    print(_atoi('73847759347583795737539759'))