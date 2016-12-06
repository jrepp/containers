#!/usr/bin/python
import inspect

def stacktrace(stack):
    for frame in stack:
        print frame
        for l in frame[0].f_locals:
            print '  locals:', l 

def definer(*args):
    print 'definer:'
    print '  ', args
    stacktrace(inspect.stack())

def emit(*args):
    print 'emit:'
    for k in args:
        print k
    stacktrace(inspect.stack())
    return definer

class Test(object):

    @emit('foo')
    def property_c(self):
        pass

    def __init__(self):
        self.propert_a = 'a'
        self.propert_b = 'a'

t = Test()
