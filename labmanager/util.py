#!/usr/bin/python
#coding:utf8

__author__ = ['markshao']

import os

try:
    from cPickle import load, dump
except ImportError:
    from pickle import load, dump


def write_json_fd(dist, fpath):
    if os.path.exists(fpath):
        os.remove(fpath)
    f = open(fpath, "wb")
    dump(dist, f)
    f.close()


def read_dict_fd(fpath):
    f = open(fpath, "rb")
    obj = load(f)
    f.close()
    return obj