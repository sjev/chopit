#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Utility functions
"""


def say_hello(n_times: int = 1):
    """print hello string

    Args:
        n_times (int, optional): number of times to print. Defaults to 1.
    """

    for idx in range(n_times):
        print(f"Hello {idx}")


if __name__ == "__main__":
    say_hello(10)
