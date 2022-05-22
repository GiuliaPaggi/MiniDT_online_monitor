import sys, random 
import copy

def sort_layers(bx_input):
    """
    This function sorts the bx for the simulated event. 
    Due to how the pin and channels number are assigned one has [L4, L2, L3, L1], 
    but bx must be increasing from L4 to L1.

    Parameters
    ----------
    bx_list : list
        List of randomly generated bx to be sorted.

    Returns
    -------
    sorted_bx_list : TYPE
        Sorted list of bx for which the bx at L4 > L3 > L2 > L1.

    """
    bx_list = copy.copy(bx_input)
    if len(bx_list) == 4: 
        bx_list.sort()
        a = bx_list[0]
        b = bx_list[2]
        c = bx_list[1] 
        d = bx_list[3]
        
        sorted_bx_list = [a, b, c, d]
        return sorted_bx_list
    else: 
        return ValueError






