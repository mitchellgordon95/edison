import os
from os.path import exists, join
import inspect
from subprocess import check_call
import types


class NoGlobals(dict):
    def __getitem__(self, key):
        if not key in vars(
                dict.__getitem__(self, '__builtins__')) and (
                    not key.startswith('__') or not key.endswith('__')):
            raise Exception('Tasks cannot access global state.'
            'Please import inside the task.')
        else:
            return dict.__getitem__(self, key)

    def get(self, key):
        if not key.startswith('__') or not key.endswith('__'):
            raise Exception('Tasks cannot access global state.'
                            ' Please import inside the task.')
        else:
            return dict.get(self, key)


class NoClosure(tuple):
    def __getitem__(self, key):
        raise Exception('Tasks cannot access closures.'
                        ' Please import inside the task.')


class Task(object):
    def __init__(self, id_, func):
        self.id_ = id_
        self.func = types.FunctionType(
            func.__code__,
            NoGlobals(func.__globals__),
            argdefs=func.__defaults__,
            closure=NoClosure())
        self.name = func.__name__




class FileName(str):
    pass


def done_fname(task):
    return join(task.name, "DONE")


def is_done(task):
    return exists(done_fname(task))


def mark_done(task):
    check_call(["touch", done_fname(task)])


# Note to self: don't worry about virtual envs when we use qsub, just make sure
# all the environment variables are the same.
def run(task):
    sig = inspect.signature(task.func)

    params = {}
    for param_name, param in sig.parameters.items():
        assert param.default == sig.empty or type(param.default) == FileName
        if param.default and param.default != sig.empty:
            fname = param.default
        else:
            fname = param.name

        params[param.name] = join(task.name, fname)

    task.func(**params)

