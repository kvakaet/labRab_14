#!usr/bin/env python3
# -*- coding: utf-8 -*-


def func(type_):
    def inner(value):
        gen = (e for e in value.split())
        if type_ == 'list':
            return list(gen)
        return tuple(gen)

    return inner


if __name__ == '__main__':
    print(func('list')('1 2 3 4'))
    print(func('tuple')('1 2 3 4 5'))
