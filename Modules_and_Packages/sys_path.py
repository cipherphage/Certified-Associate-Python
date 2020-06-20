import sys

# How Python knows where to find modules (AKA the search path):
# - The directory containing the running script is automatically the first item 
#   in the search path. When running the REPL this will be the current directory.
# - The values set in the PYTHONPATH environment variable (if it is set) will be 
#   next in the list.
# - Finally, a list of directories configured when Python was installed. This 
#   list contains paths to directories that have the standard library modules and 
#   other packages we've installed.
# Note: Python will search for a built-in module by name before searching the paths 
# in sys.path. This means you can't accidentally create a module with the same name 
# as a built-in module, which prevents you from overwriting the built-in module.

print(sys.path)