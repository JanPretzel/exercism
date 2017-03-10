#
# Skeleton file for the Python "Hello World" exercise.
#


def hello(name=''):
    if not name:
        name = "World"

    return 'Hello, {}!'.format(name)
