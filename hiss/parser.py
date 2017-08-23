#!/usr/bin/env python
#
# Base of hiss implementations
#
# this is part of hiss. https://github.com/KennethanCeyer/hiss
#
# (C) 2017-2017 Kenneth Ceyer <kennethan@nhpcw.com>
# this is distributed under a free software license, see LICENSE

import abc


class BaseParser(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def _process(self, args):
        return NotImplemented

    @abc.abstractmethod
    def define_commands(self):
        return NotImplemented


    @abc.abstractmethod
    def define_arguments(self):
        return NotImplemented
