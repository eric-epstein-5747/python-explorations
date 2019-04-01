def findAnEven(L):
    """Assumes L is a list of integers
       Returns the first even number in L
       Raises ValueError if L does not contain an even number"""
    i = 0
    while i < len(L):
        if L[i]%2 == 0:
            return L[i]
            break
        if i+1 == len(L):
            raise ValueError('L does not contain an even number.')
        i = i + 1
        