#Write a function isIn that accepts two strings as arguments and returns True if either string occurs anywhere in the other, and False otherwise. 
def isIn(x, y): 
    if x in y:
        return True
    elif y in x:
        return True
    else:
        return False