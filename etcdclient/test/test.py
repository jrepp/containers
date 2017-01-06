#!/usr/bin/python

import sys
import etcd
import unittest
import os
import inspect

#
# Fix up import path if running directly
#
if __name__ == '__main__':
    thispath = os.path.dirname(inspect.getfile(inspect.currentframe()))
    print 'this path', thispath
    sys.path += os.path.join(thispath, '..')

#
# Test modules registered here
#
import test_basic
import test_prop
import test_command
import test_service
import test_command

def run():
    all_tests = unittest.TestSuite([
        basic_test.suite(),
        prop_test.suite(),
        cluster_test.suite(),
        service_test.suite(),
        command_test.suite(),
    ])

    unittest.main()
    
if __name__ == '__main__':
    run()

