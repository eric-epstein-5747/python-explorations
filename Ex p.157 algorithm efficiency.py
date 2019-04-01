# The question concerns the following search algorithm: 

def search(L, e):
    """Assumes L is a list, the elements of which are in ascending order.
    Returns True if e is in L and False otherwise."""
    
    def bSearch(L, e, low, high): 
        #Decrements high - low
        if high == low:
            return L[low] == e
        mid = (low + high)//2
        if L[mid] == e:
            return True
        elif L[mid] > e:
            if low == mid: #nothing left to search
                return False
            else:
                return bSearch(L, e, low, mid - 1)
        else:
            return bSearch(L, e, mid + 1, high)
    
    if len(L) == 0:
        return False
    else: 
        return bSearch(L, e, 0, len(L)-1)

# The question is: Why does the code use mid+1 rather than mid 
# in the second recursive call?
#
# Answer: The second call occurs in the case where L[mid] < e. So we know 
# at this point that if e is in L then L[mid] < e <= L[high]. So we now 
# restrict our search to the top half of the interval [low, high]. Since by 
# this point we already know that L[mid] != e, we can ignore L[mid] and 
# start looking at the next value of L, L[mid + 1].