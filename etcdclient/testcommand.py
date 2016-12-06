#!/usr/bin/env python

import sys

import command_runner as _cr
import start as _start
from context import Context

c = _start.setup_client()
if c is None:
    print 'ensure your environment is setup correctly'
    sys.exit(1)


ctx = Context(c)
runner = _cr.CommandRunner(u'commands', ctx)
runner.add('foo')
runner.add('bar')
runner.update()

