def fn_doc():
        '''
        Here is the docstring of the python function, here we need to check whether the length of docstring is less then
        50 or not , will check this with the help of closure.'''

def doc_func(fn_doc):
    '''Write a closure that takes a function and then check whether the function passed has a docstring with more 
    than 50 characters. 50 is stored as a free variable '''
    doc_len = 50
    
    def doc_string_count():
        if(len(fn_doc.__doc__) >= doc_len):
            return True
        return False
        
    return doc_string_count


def fibgen():
    ''' This fucntion is used to generate fibonnaci numbers, using the closure method'''
    fib_tup = 0
    
    def next_fib():
        nonlocal fib_tup
        if(fib_tup == 0):
            fib_tup = 0,1
            
        else:
            tmp1 = fib_tup[1]
            fib_tup = tmp1,fib_tup[1] +fib_tup[0]
            
        return fib_tup[-1]
    
    return next_fib


def add(a, b):
    '''Function adds the two elements
    Input : a,b int object
    '''
    return a + b

def mult(a, b, c):
    '''Function which return the product of the numbres
    Inputs: a,b,c int object
    '''
    return a * b * c

def div(a, b):
    ''' Div of two numbers
    a : int
    b : int
    '''
    if b==0:
        raise ValueError("denomnetor should not be zero")
    else:
        return a/b


counters = dict()
def global_dictionary_variable_with_the_counts(fn):
    '''Function which keep tracks the how many times a function were called
    Input:
    count: initialze
    '''
    cnt = 0
    def inner(*args, **kwargs):
        nonlocal cnt
        cnt += 1
        counters[fn.__name__] = cnt
        return fn(*args, **kwargs)
    return inner



def counter(fn, counters):
  """This function useses a closure to passdifferent dictionary variables
    to update different dictionaries.
  """

  cnt = 0
  def inner(*args, **kwargs):
    nonlocal cnt
    cnt += 1
    counters[fn.__name__] = cnt
    return fn(*args, **kwargs)
  return inner
