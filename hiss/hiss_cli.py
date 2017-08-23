#!/usr/bin/env python
#
# Base of hiss implementations
#
# this is part of hiss. https://github.com/KennethanCeyer/hiss
#
# (C) 2017-2017 Kenneth Ceyer <kennethan@nhpcw.com>
# this is distributed under a free software license, see LICENSE

import sys
import os
import argparse
from hiss import config, parser
from hiss.utils import exceptions, tools
from hiss.parsers import init


class Hiss(parser.BaseParser):
    """this is a definition for parsing command."""
    def __init__(self, *argv):
        """define argparse and process"""
        self.parser = argparse.ArgumentParser(
            prog=config.PROG,
            description=config.DESCRIPTION)

        self.define_parsers()
        self.define_commands()
        self.define_arguments()

        self._receive(*argv)

    def _receive(self, *argv):
        """receive argument from sys"""
        args = self.parser.parse_args(*argv)
        self._process(args)
        self._process_propagation(args)

    def _process(self, args):
        """process arguments and subcommands"""
        # -v, --version
        if args.version is True:
            tools.print_version()

    def _process_propagation(self, args):
        """propagation arguments to subparsers"""
        # init
        self.parser_init._process(args)

    def define_parsers(self):
        """define all subparsers using add_subparsers"""
        """todo: create default commands; init, add, show, list"""
        self.subparser = self.parser.add_subparsers(
            dest='process')

        # init
        self.parser_init = init.Parser(self.subparser)

    def define_commands(self):
        """define all tasks using add_parser"""
        pass

    def define_arguments(self):
        """define all arguments to argparse"""
        _type = 'argument'

        # -v, --version
        self.parser.add_argument(
            '-v', '--version', help='show version', action='store_true')


def main():
    """start hiss"""
    Hiss(sys.argv[1:])

if __name__ == '__main__':
    main()
