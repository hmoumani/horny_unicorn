def ft_reduce(function_to_apply, iterable):
    """Apply function of two arguments cumulatively.
    Args:
    function_to_apply: a function taking an iterable.
    iterable: an iterable object (list, tuple, iterator).
    Return:
    A value, of same type of elements in the iterable parameter.
    None if the iterable can not be used by the function.
    """
    if not callable(function_to_apply):
        raise TypeError("Function is not callable.")
    elif not hasattr(iterable, '__iter__'):
        return None
    elif iterable:
        result = iterable[0]
        for i in iterable[1:]:
            result = function_to_apply(result, i)
        return result
    
