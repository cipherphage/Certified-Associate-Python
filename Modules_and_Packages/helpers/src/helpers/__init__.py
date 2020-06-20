"""
Helpers is a package that provides easy to use helper functions
and variables.
"""

# if we restrict this module's
# module entities to only extract_upper then
# extract_lower cannot be exported with *
# however, it can still be accessed directly (see main.py)
__all__ = ["extract_upper"]

# this will make strings available directly from the helpers module
# instead of needing to do helpers.strings, but note that we are 
# restricting __all__ so if we want access to a module entity not
# in the __all__ list then we still need to do helpers.strings
from .strings import *

# Note: While the PCAP syllabus doesn't actually mention implicit namespace 
# packages, it is worth noting that they exist. As of Python 3.3, if we're 
# creating a package that doesn't need to do anything with the __init__.py, then 
# we can skip creating the __init__.py entirely and our package will work just fine.