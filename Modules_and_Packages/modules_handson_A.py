from random import shuffle as l_shuffle

def reverse(str):
    # this is slower: ''.join(reversed(str))
    '''
    reverse takes a string and returns
    the string reversed

    >>> reverse("Hello World")
    'dlroW olleH'
    '''
    return str[::-1]

def shuffle(str):
    '''
    reverse takes a string and returns
    the string reversed

    need a different test for this one!
    >>> shuffle("Hello World")
    'llr ldoeHWo'
    '''
    slist = list(str)
    l_shuffle(slist)
    return ''.join(slist)