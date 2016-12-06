#!/usr/bin/python

import etcd
import sys
import os
import pprint

import test as _test

def print_tree(t):
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(t)

def setup_client():
    addr = os.getenv('ETCD_ADDR')
    port = int(os.getenv('ETCD_PORT', 0))
    if not addr or not port:
        return None
    client = etcd.Client(
            host=addr,
            port=port,
            allow_reconnect=True,
            allow_redirect=True)
    return client

def main():
    client = setup_client()
    if not client:
        print 'usage: ETCD_ADDR=<addr> ETCD_PORT=port ./start.py'
        sys.exit(1)
    _test.test(client)
    
if __name__ == '__main__': 
    main()
