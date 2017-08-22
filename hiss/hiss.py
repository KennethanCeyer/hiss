#!/usr/bin/env python
#
# Base of hiss implementations
#
# this is part of hiss. https://github.com/KennethanCeyer/hiss
#
# (C) 2017-2017 Kenneth Ceyer <kennethan@nhpcw.com>
# this is distributed under a free software license, see LICENSE

import sys
import argparse
import config
from cli import exceptions, tools


class Hiss(object):
    """this is a definition for parsing command."""
    def __init__(self, *argv):
        self.parser = argparse.ArgumentParser(
            prog=config.PROG,
            description=config.DESCRIPTION)

        self.define_commands()
        self.define_arguments()
        
        args = self.parser.parse_args(*argv)
        self._process(args)

    def _process(self, args):
        """process arguments and subcommands"""

        # -v, --version
        if args.version is True:
            tools.print_version(config.VERSION)

    def define_commands(self):
        """todo: create default commands; init, add, show, list"""

    def define_arguments(self):

        _type = 'argument'

        # -v, --version
        self.parser.add_argument(
            '-v', '--version', help='show version', action='store_true')
Hiss(sys.argv[1:])
