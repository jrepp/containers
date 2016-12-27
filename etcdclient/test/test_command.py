#!/usr/bin/env python

import sys

import command_runner as _cr
import start as _start
from app import App

ctx = App('testcommand')
runner = _cr.CommandRunner(u'commands', ctx)
runner.add('foo')
runner.add('bar')
runner.update()

