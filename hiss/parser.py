#!/usr/bin/env python
#
# base of hiss implementations
#
# this is part of hiss. https://github.com/KennethanCeyer/hiss
#
# (C) 2017-2017 Kenneth Ceyer <kennethan@nhpcw.com>
# this is distributed under
# Apache 2.0 <https://www.apache.org/licenses/LICENSE-2.0>

import abc
import six


@six.add_metaclass(abc.ABCMeta)
class BaseParser():
    @abc.abstractmethod
    def _process(self, args):
        return NotImplemented

    @abc.abstractmethod
    def define_commands(self):
        return NotImplemented

    @abc.abstractmethod
    def define_arguments(self):
        return NotImplemented
