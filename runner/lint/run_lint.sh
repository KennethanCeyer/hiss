#!/usr/bin/env bash
#
# this is runner file for linting python package
#
# (C) 2017-2017 Kenneth Ceyer <kennethan@nhpcw.com>
# this is distributed under
# Apache 2.0 <https://www.apache.org/licenses/LICENSE-2.0>

path="$PWD/hiss"

pycodestyle "$path"

