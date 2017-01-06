import unittest
import inspect

def output(s):
    #print s
    pass


def stacktrace(stack):
    for frame in stack:
        output(frame)
        for l in frame[0].f_locals:
            output('  locals: {0}'.format(l))


def definer(*args):
    output('definer:')
    output('  {0}'.format(args))
    stacktrace(inspect.stack())


def emit(*args):
    output('emit:')
    for k in args:
        output(k)
    stacktrace(inspect.stack())
    return definer

        
class TestProperty(unittest.TestCase):
    @emit('foo')
    def property_c(self):
        pass

    def test_self(self):
        pass


def suite():
    tests = ['test_self']
    return unittest.TestSuite(map(TestProperty, tests))

