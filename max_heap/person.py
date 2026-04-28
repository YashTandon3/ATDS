#!/usr/bin/env python3

__author__ = "Yash Tandon"
__version__ = "2026-04-27"


class Person:
    def __init__(self, name, vip_value):
        self.__name = name
        self.__vip_value = vip_value

    def get_name(self):
        return self.__name

    def get_vip_value(self):
        return self.__vip_value

    def __str__(self):
        return f"{self.__name}:{self.__vip_value}"