#!/usr/bin/python3

import os
import inspect


def get_input(input_file):
    func_dir = os.path.dirname(inspect.stack()[1].filename)
    input = os.path.join(func_dir, input_file)
    with open(input) as f:
        s = f.read()
    return s
