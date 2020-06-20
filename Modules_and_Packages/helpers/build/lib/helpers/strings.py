
def extract_upper(phrase):
    return list(filter(str.isupper, phrase))

def extract_lower(phrase):
    return list(filter(str.islower, phrase))

# we can create a "hidden" variable using an underscore
# this will mean it's not exported with *
# however, it can still be accessed directly (see main.py)
_hidden = "hidden"

# will print "helpers"
print(f"__name__ in strings.py: {__name__}")

# This conditional will only print if the context
# is __main__. So when we import helpers elsewhere and
# run it this condition is not met, but when we
# run helpers.py directly (i.e., python helpers.py)
# then this condition is met: it is running in the
# main context then.
if __name__ == "__main__":
    print("HELLO FROM STRINGS IN HELPERS")