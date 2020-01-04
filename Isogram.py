def is_isogram(string):
    """
    An isogram is a word that has no repeating letters, 
    consecutive or non-consecutive. 
    Implement a function that determines whether 
    a string that contains only letters is an isogram. 
    Assume the empty string is an isogram. Ignore letter case.
    is_isogram("Dermatoglyphics" ) == true
    is_isogram("aba" ) == false
    is_isogram("moOse" ) == false
    """
    return len(list(string)) == len(set(string.upper()))

if __name__ == "__main__":
    print(is_isogram("Dermatoglyphics"))
    print(is_isogram("aba")) 
    print(is_isogram("moOse"))