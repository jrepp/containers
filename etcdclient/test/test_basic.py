#!/usr/bin/env python

import time
import unittest

import start
import app
import service_desc as sdesc
import service_discovery as sd

class TestFind(unittest.TestCase):
    def test_find_by_type(self):
        c = start.setup_client()
        app = app.App(c)
        s = sdesc.test_service(ctx)
        c.write(s.path(), s.to_json(), ttl=3)
        #results = c.read('/services/global')
        duration = 2
        start = time.time()
        while (time.time() - start) > duration:
            results = sd.find_by_type(s, ctx)
            if len(results) == 0:
                break
            time.sleep(.5)
            print results


