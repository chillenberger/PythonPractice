# decorators take other functions and wrap them to change output. 
# functools is needed to preserve function name 

import functools
import logging

def decorator_func(f):
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        print('in decorator')
        f(*args, **kwargs)
        print('bye')
    return wrapper 

@ decorator_func
def my_func():
    print('in my function')

@logging.Logger
def test():
    print('test')

if __name__ == '__main__':
    my_func()
    test()