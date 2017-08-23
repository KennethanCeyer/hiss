#!/usr/bin/env python
#
# Base of hiss implementations
#
# this is part of hiss/cli. https://github.com/KennethanCeyer/hiss
#
# (C) 2017-2017 Kenneth Ceyer <kennethan@nhpcw.com>
# this is distributed under a free software license, see LICENSE

import requests
import json
from hiss import __version__

_FORMAT_VERSION = 'hiss version {version}'


def print_version():
    """display current version"""
    print(_FORMAT_VERSION.format(version=__version__))
