def sumDigits(s): 
    """Assumes s is a string
       Returns the sum of the decimal digits in s
            For example, if s is 'a2b3c' it returns 5"""
    summ = 0
    for i in s: 
        try: 
            int(i)
            summ = summ + int(i)
            
        except ValueError:
            summ = summ

    return summ 