#!/usr/bin/python

import etcd
import sys
import os
import pprint

import application as _application
import test.test as _test

def print_tree(t):
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(t)


def main():
    # Setup client explicitly
    client = _application.default_client()
    if not client:
        print 'usage: ETCD_ADDR=<addr> ETCD_PORT=port ./start.py'
        sys.exit(1)

    properties = {
        'git-branch': 'master',
        'git-commit': '0badfood',
        'hostname': 'host.name.com'
    }

    with _application.Application("start", client, **properties) as app:
        _test.run()
    
if __name__ == '__main__': 
    main()
