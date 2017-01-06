import unittest

import application as _application

template = """
{
    "type": "service",
    "name": "test",
    "service_class": "worker-a",
    "provides": ["a", "b", "c"],
    "region": "jrepp-test2",
    "ip": "192.168.0.10",
    "ports": [5000,5001],
    "site": "main",
    "cluster": "test-cluster"
}"""

class TestSingleService(unittest.TestCase):
    def test_from_template(self):
        with _application.default() as app:
            s = app.from_json(template)


def suite():
    tests = ['test_from_template']
    return unittest.TestSuite(map(TestSingleService, tests))
