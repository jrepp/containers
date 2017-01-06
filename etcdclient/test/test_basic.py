import time
import unittest

import application as _application
import common as _common

class TestFind(unittest.TestCase):
    def test_find_by_type(self):
        app = _application.default()
        s = _common.test_service(app)
        app.etcd_client.write(s.path(), s.to_json(), ttl=3)

        #results = c.read('/services/global')

        duration = 2
        start = time.time()
        while (time.time() - start) > duration:
            results = app.discovery.find_by_type(s, ctx)
            if len(results) == 0:
                break
            time.sleep(.5)
            print results

def suite():
    tests = ['test_find_by_type']
    return unittest.TestSuite(map(TestFind, tests))
