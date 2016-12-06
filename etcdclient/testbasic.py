#!/usr/bin/python

import time

import start
import context
import service_desc as sdesc
import service_discovery as sd


c = start.setup_client()
ctx = context.Context(c)
s = sdesc.test_service(ctx)
c.write(s.path(), s.reflect(), ttl=3)
#results = c.read('/services/global')

while True:
    results = sd.find_by_type(s, ctx)
    if len(results) == 0:
        break
    time.sleep(.5)
    print results
