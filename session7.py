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


# func_counter ={'add':0,'mul':0,'div':0}

# def add(a, b):
#     '''Function adds the two elements
#     Input : a,b int object
#     '''
#     return a + b

# def mul(a, b):
#     '''Function which return the product of the numbres
#     Inputs: a,b int object
#     '''
#     return a*b

# def div(a, b):
#     ''' Div of two numbers
#     a : int
#     b : int
#     '''
#     return a / b

# add_c,mul_c,div_c = 0,0,0

# def outer_track(fn):
#     '''a closure that counts how many times a function was called. Write a new one that can keep a track of how many times 
#     add/mul/div functions were called, and update a global dictionary variable with the counts '''

#     def func_count_tracker():
    
#         global func_counter
#         global add_c
#         global div_c
#         global mul_c
        
#         if(fn.__name__=='mul'):
#             mul_c += 1
#             func_counter[fn.__name__] = mul_c
            
#         if(fn.__name__=='add'):
#             add_c += 1
#             func_counter[fn.__name__] = add_c
            
#         if(fn.__name__=='div'):
#             div_c += 1
#             func_counter[fn.__name__] = div_c
   
#         return func_counter
    
#     return func_count_tracker

# def outer_track_diff(fn,dict_c):
#     '''we can pass in different dictionary variables to update different dictionaries '''

#     def func_count_tracker_diff():
        
#         if(fn.__name__=='mul'):
            
#             dict_c[fn.__name__] += 1
            
#         if(fn.__name__=='add'):
            
#             dict_c[fn.__name__] +=  1
            
#         if(fn.__name__=='div'):
            
#             dict_c[fn.__name__] += 1
   
#         return dict_c
    
#     return func_count_tracker_diff




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

def my_counter(fn):
    '''This function used to calcualte how many times a funtion is called
    '''
    cnt = 0
    def inner(*args,**kwargs):
        nonlocal cnt
        cnt+=1
        return cnt
    return inner

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

c = dict()
m = dict()
d = dict()