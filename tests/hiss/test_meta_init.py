#!/usr/bin/env python
#
# test code
#
# this is part of hiss. https://github.com/KennethanCeyer/hiss
#
# (C) 2017-2017 Kenneth Ceyer <kennethan@nhpcw.com>
# this is distributed under
# Apache 2.0 <https://www.apache.org/licenses/LICENSE-2.0>


from utils.util_file import  find_var


def test_author():
    # why: __init__.author will be never change
    file_name = 'hiss/__init__.py'
    _var_name = '__author__'
    expected = 'Kenneth Ceyer <kennethan@nhpcw.com>'
    assert find_var(file_name, var_name=_var_name) == expected
