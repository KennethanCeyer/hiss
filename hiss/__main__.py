#!/usr/bin/env python
#
# portable serial port access with python
# this is a main file, part of hiss.
#
# (C) 2017-2017 Kenneth Ceyer <kennethan@nhpcw.com>
# this is distributed under a free software license, see LICENSE

import sys
from hiss.hiss_cli import main


if __name__ == '__main__':
    sys.exit(main())