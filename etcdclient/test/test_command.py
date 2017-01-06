#!/usr/bin/env python

import sys
import unittest

import command as _command
import application as _application

class TestCommand(unittest.TestCase):
    def test_single_command(self):
        app = _application.default('testcommand')
        runner = _command.Runner(u'commands', app)
        runner.add('foo')
        runner.add('bar')
        runner.update()

def suite():
    tests = ['test_single_command']
    return unittest.TestSuite(map(TestCommand, tests))
