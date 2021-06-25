import math
from functools import reduce
import random
import string
from functools import partial
import session7
import pytest
import re
import math
import os
import inspect
import unittest

README_CONTENT_CHECK_FOR = ["global","local","non local","free variable","closure","cell"]

def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"

def test_readme_contents():
    readme = open("README.md", "r",encoding = 'utf-8')
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 100, "Make your README.md file interesting! Add atleast 100 words"

def test_readme_proper_description():
    READMELOOKSGOOD = True
    f = open("README.md", "r",encoding = 'utf-8')
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"

def test_readme_file_for_formatting():
    f = open("README.md", "r",encoding = 'utf-8')
    content = f.read()
    f.close()
    assert content.count("#") >= 10


def test_function_name_had_cap_letter():
    functions = inspect.getmembers(session7, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"
        
def test_fibonnaci_positive():
    fn=session7.fibgen()
    fib_list = []
    org_list = [1,1, 2, 3, 5, 8, 13, 21, 34, 55]
    for i in range(10):
        fib_list.append(fn())
        
    assert True== (sorted(fib_list)== sorted(org_list)), "Fibonnaci function not working proper"

    
def test_fibonnaci_negative():
    fn=session7.fibgen()
    fib_list = []
    org_list = [1, 2, 3, 5, 8, 14, 22, 35, 57, 92]
    for i in range(10):
        fib_list.append(fn())
        
    assert False== (sorted(fib_list)== sorted(org_list)), "passed series is not a Fibonnaci series"
    
def test_add():
    assert session7.add(10, 20) == 30, "inncorrect addtion of two numbers"
	
def test_mult():
    assert session7.mult(10, 20,1) == 200, "incorrect multiplication of three numbers"
	
def test_div():
    assert session7.div(100, 4) == 25.0, "inncorrect division of two numbers"

def test_counter():
    c = dict()
    m = dict()
    d = dict()
    c_val, m_val, d_val = {'add':4},{'mult':3},{'div':2}
    fn = session7.add
    value =session7. counter(fn, c)
    value(1,2),value(1,2),value(1,2),value(1,2)
    fn = session7.mult
    value = session7.counter(fn, m)
    value(2,3,1),value(2,3,1),value(2,3,1)
    fn = session7.div
    value = session7.counter(fn, d)
    value(4, 2),value(4, 2)
    assert c == c_val,'count how many times each funtion is called..'
    assert m == m_val,'count how many times each funtion is called..'
    assert d == d_val,'count how many times each funtion is called..'


def test_doc_func():
    a1 = session7.doc_func(session7.fn_doc)
    assert True == a1(), "some is wrong, bring your vocab out"


def test_check_free():
    fn=session7.fibgen()
    assert ('fib_tup',) == fn.__code__.co_freevars,"free variable needed"

def test_closure_fibgen():
    fn=session7.fibgen()
    assert True == (fn.__closure__ != "") ,"use closure"

def test_closure_doc_func():
    a1 = session7.doc_func(session7.fn_doc)
    assert True == (a1.__closure__ != "") ,"use closure"


def test_function_doc_strings():
    """
    Test case to check the docstrings are included in the function definition.
    """
    functions = inspect.getmembers(session7, inspect.isfunction)
    for function in functions:
        assert function[1].__doc__



def test_closure_global_dictionary_variable_with_the_counts():
    fn = session7.add
    f1 = session7.global_dictionary_variable_with_the_counts(fn)
    assert bool(f1.__closure__)==True, 'Closure is missing'
    
