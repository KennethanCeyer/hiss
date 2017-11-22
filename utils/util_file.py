import re
import io
from os import path


def read(*names, **kwargs):
    """
    python 2 and python 3 compatible text file reading.
    required for single-sourcing the version string.
    """
    with io.open(
        path.relpath(path.join(*names)),
        encoding=kwargs.get("encoding", "utf8")
    ) as fp:
        return fp.read()


def find_version(*file_paths):
    _var_name = "__version__"
    return find_var(*file_paths, var_name=_var_name)


def find_var(*file_paths, var_name):
    file = read(*file_paths)
    match = re.search(r"^%s = ['\"]([^'\"]*)['\"]" % var_name, file, re.M)

    if match:
        return match.group(1)
    raise RuntimeError("Unable to find version string.")
