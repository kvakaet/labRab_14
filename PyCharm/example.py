#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def add_four(a):
    x = 2

    def add_some():
        print("x = " + str(x))
        return a + x

    return add_some()


if __name__ == '__main__':
    print(add_four(5))
