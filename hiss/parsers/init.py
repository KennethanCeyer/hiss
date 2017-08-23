#!/usr/bin/env python
#
# Base of hiss implementations
#
# this is part of hiss/cli. https://github.com/KennethanCeyer/hiss
#
# (C) 2017-2017 Kenneth Ceyer <kennethan@nhpcw.com>
# this is distributed under a free software license, see LICENSE

import argparse
from hiss import parser


NAME = 'init'
DESCRIPTION = 'init repository on current path'


class Parser(parser.BaseParser):
    def __init__(self, parser):
        self.subparser = parser
        self.define_commands()
        self.define_arguments()

    def _process(self, args):
        """process arguments and subcommands"""
        if args.process != NAME:
            return

        print('init')

    def define_commands(self):
        self.parser = self.subparser.add_parser(NAME, description=DESCRIPTION)

    def define_arguments(self):
        pass
