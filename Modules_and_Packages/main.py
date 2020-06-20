# IMPORT _ AS _
# import helpers as h

# name = "Keith Thompson"
# print(f"Lowercase letters: {h.extract_lower(name)}")
# print(f"Uppercase letters: {h.extract_upper(name)}")

# FROM _ IMPORT _, _ AS _
# from helpers import extract_lower, extract_upper

# name = "Keith Thompson"
# print(f"Lowercase letters: {extract_lower(name)}")
# print(f"Uppercase letters: {extract_upper(name)}")

# use a shebang to reference the executable
# don't forget to chmod +x main.py
#!/usr/bin/env python

# FROM _ IMPORT ALL
from helpers import *
from helpers.strings import extract_lower, _hidden
from helpers import variables
import helpers

# Will print __main__ because we are running
# python main.py which runs this in the main
# context. The imported modules will not be
# in the main context
print(f"__name__ in main.py: {__name__}")

print(f"Lowercase letters: {extract_lower(variables.name)}")
print(f"Uppercase letters: {extract_upper(variables.name)}")
print(f"From helpers: {helpers.strings.extract_lower(_hidden)}")

print(helpers.__doc__)
# once we've built our helpers wheel we can pip install helpers:
# pip install helpers/dist/helpers-1.0.0-py3-none-any.whl