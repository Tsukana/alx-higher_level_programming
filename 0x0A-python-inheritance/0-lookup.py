#!/usr/bin/python3
'''Modul for lookup method.'''


def lookup(obj):
    '''Looks up.object attributes and Methods.
    Args:
        obj : The obj to list.

      Returns:
        list : The list of attributes
        '''
    return dir(obj)
