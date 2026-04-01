"""
A collection of simple math operations
"""



def simple_add(a,b):
    """
    summation of two numbers
    ---------------
    Parameters
    --------
    a : numerical
    b : numerical
    inordered
    ------
    returns 
    ------
    int
        sum of a and b
        a+b
    """
    
    return a+b

def simple_sub(a,b):
    """
    subtraction of two numbers
    ---------------
    Parameters
    --------
    a : numerical
    b : numerical
    ------
    returns 
    ------
    int
        subtraction of b from a
        a-b
    """
    
    return a-b

def simple_mult(a,b):
    """
    multiplication of two numbers
    ---------------
    Parameters
    --------
    a : numerical
    b : numerical
    ------
    returns 
    ------
    int
        multiplication of a and b
        a*b
    """
    
    return a*b

def simple_div(a,b):
    """
    division of two numbers
    ---------------
    Parameters
    --------
    a : numerical
    b : numerical
    ------
    returns 
    ------
    int
        division of a over b
        a/b
    """

    return a/b

def poly_first(x, a0, a1):
    """
    computes the value of a first order polynomial at position x
    ---------------
    Parameters
    --------
    x : numerical
        x value where to compute polynomial value
    a0 : numerical
        first value of polynomial
    a1 : numerical
        second value of polynomial
    ------
    returns 
    ------
    int
        polynomial value at location x
        a0 + a1*x
    """    
    return a0 + a1*x

def poly_second(x, a0, a1, a2):
    """
    computes the value of a second order polynomial at position x
    ---------------
    Parameters
    --------
    x : numerical
        x value where to compute polynomial value
    a0 : numerical
        first value of polynomial
    a1 : numerical
        second value of polynomial
    a2 : numerical
        third value of polynomial
    ------
    returns 
    ------
    int
        polynomial value at location x
        a0 + a1*x +  a2 * x^2
    """ 
    return poly_first(x, a0, a1) + a2*(x**2)

# Feel free to expand this list with more interesting mathematical operations...
# .....
