# coding: utf-8

# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.

from __future__ import unicode_literals

from six import string_types


def strings_to_lists(obj):
    if isinstance(obj, dict):
        return {k: strings_to_lists(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [strings_to_lists(v) for v in obj]
    elif isinstance(obj, string_types):
        return obj.splitlines(True)
    else:
        return obj


def revert_strings_to_lists(obj):
    if isinstance(obj, dict):
        return {k: revert_strings_to_lists(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        if not obj:
            return obj
        elif isinstance(obj[0], string_types):
            return "".join(obj)
        else:
            return [revert_strings_to_lists(v) for v in obj]
    else:
        return obj


def split_path(path):
    "Split a path on the form /foo/bar into ['foo','bar']."
    return [x for x in path.strip("/").split("/") if x]


def join_path(*args):
    "Split a path on the form /foo/bar into ['foo','bar']."
    if len(args) == 1 and isinstance(args[0], (list, tuple, set)):
        args = args[0]
    assert len(args) > 1, "Nothing to join"
    args = [a for a in args if a not in ["", "/"]]
    ret = "/".join(args)
    return ret if ret.startswith("/") else "/" + ret
