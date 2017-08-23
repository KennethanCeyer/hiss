#!/usr/bin/env python
#
# Base of hiss implementations
#
# this is part of hiss/cli. https://github.com/KennethanCeyer/hiss
#
# (C) 2017-2017 Kenneth Ceyer <kennethan@nhpcw.com>
# this is distributed under a free software license, see LICENSE

_FORMAT_GENERAL = 'error: {}'
_FORMAT_ERRNO = 'error: (errorno {}) {}'


def _get_message(message, errno):
    _current_format = _FORMAT_GENERAL
    if errno is not None:
        _current_format = _FORMAT_ERRNO
    return _current_format.format(message, errno)
        

class GeneralException(Exception):
    def __init__(self, message, errno):
        self.message = message
        self.errno = errno
    
    def __str__(self):
        return _get_message(self.message, self.errno)
