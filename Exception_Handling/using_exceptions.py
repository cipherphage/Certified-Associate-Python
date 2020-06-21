import sys

from cli import main
from cli.errors import ArgumentError

try:
    main()
except (ArgumentError, AssertionError) as err:
    print(f"Error: {err}")
    sys.exit(1)

# NOTES:
#
# The Python parser can remove assert statements when our script 
# is run with the -O or -OO flags (capital `o' for "optimize").
#
# When we use the -O or -OO flags, we optimize our code to remove 
# assertions (and docstrings with -OO), so we can't reliably use 
# asserts to determine if we're going to raise errors.