#!/usr/bin/python2


def enum(**enums):
    return type('Enum', (), enums)
    
