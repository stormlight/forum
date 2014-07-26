# -*- coding: utf-8 -*-

"""
Import Tools
============

"""

import pkgutil
import importlib


def import_submodules(package, modules=None, ignore=None):
    """Imports all submodules of a package.

    :type package: module
    :param modules: Names of modules to import.
    :type modules: list
    :param ignore: Names of modules to ignore.
    :type ignore: list
    :return: Imported modules and their names.
    :rtype: tuple
    """
    path = package.__path__
    imported_modules = []

    for loader, name, is_package in pkgutil.iter_modules(path):
        if modules and name not in modules:
            continue
        if ignore and name in ignore:
            continue
        module = importlib.import_module('.' + name, package.__name__)
        imported_modules.append((module, name))

    return imported_modules
