import re

def f(s): 
    return bool(re.findall(r"e{2,}", s))
