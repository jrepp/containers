#!/usr/bin/env python

from app import App

template = """
{
    "type": "service"
    "name": "test",
    "service_class": "worker-a"
    "region": "jrepp-test2",
    "site": "main",
    "cluster": "test-cluster"
}"""

with App() as a:
    svc = a.from_json(template)
    a.update_loop()
