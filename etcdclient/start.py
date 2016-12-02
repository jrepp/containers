#!/usr/bin/python

import etcd
import sys
import os
import pprint

def print_tree(t):
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(t)

def main():
    addr = os.getenv('ETCD_ADDR')
    port = int(os.getenv('ETCD_PORT'))

    if not addr or not port:
        print 'usage: ETCD_ADDR=<addr> ETCD_PORT=port ./start'
        sys.exit(1)

    client = etcd.Client(host=addr, port=port)

    key = '/'
    try:
        t = client.read(key, recursive=True)
        print_tree(t)
    except etcd.EtcdKeyNotFound:
        print "key not found:", key

if __name__ == '__main__': main()
