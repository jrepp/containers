import sys
import etcd
import unittest
import os
import inspect

import test_basic
import test_command
import test_prop
import test_service

if __name__ == '__main__':
    thispath = os.path.dirname(inspect.getfile())
    sys.path += os.path.join(thispath, '..')
    unittest.main()
