# coding=utf-8
__author__ = 'Anatoli Kalysch'

import importlib.util
import sys
import os


F_DIR = os.environ["VMAttack"]
F_NAME = "VMAttack.py"
sys.path.append(F_DIR)


def load_source(modname, filename):
    loader = importlib.machinery.SourceFileLoader(modname, filename)
    spec = importlib.util.spec_from_file_location(modname, filename, loader=loader)
    module = importlib.util.module_from_spec(spec)
    # The module is always executed and not cached in sys.modules.
    # Uncomment the following line to cache the module.
    sys.modules[module.__name__] = module
    loader.exec_module(module)
    return module

plugin_path = os.path.join(F_DIR, F_NAME)
plugin = load_source(__name__, plugin_path)



PLUGIN_ENTRY = plugin.PLUGIN_ENTRY
