"""Define a decorator that enforces real-valued parameter values."""
import functools


def is_real(x) -> bool:
    """
    Return True if x is real-valued; False otherwise.
    
    Usage examples:
    >>> is_real(3)
    True
    >>> is_real(3.1)
    True
    >>> is_real(3j)
    False
    >>> is_real("string")
    False
    """
    # ints and floats are considered real-valued.
    real = (int, float)  
    return isinstance(x, real)


def real_params(f):
    """
    Raise a TypeError if any arguments to f are not real-valued.

    This function is intended as a decorator.
    """
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        params = list(args) + list(kwargs.values())
        for param in params:
            if not is_real(param):
                raise TypeError(
                    f'Expected real value, got {param}'
                )
        return f(*args, **kwargs)
    return wrapper


if __name__ == '__main__':
    print(__doc__)
