"""python module to demonstrate the use of modules and packages"""

def is_pal(word:str):
    '''return True is the word is a palindrome, 
    or False if not'''
    # return bool(word == "".join([i for i in reversed(word)]))
    return word == word[::-1]

def greet(name = "world"):
    """say hello to what ever name is passed"""
    print("hello " + name)