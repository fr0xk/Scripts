import sys

def helloWorld(*objects, sep=' ', end='\n', file=sys.stdout, flush=False):
    if file is None:
        return

    object_strings = map(str, objects)
    output = sep.join(object_strings) + end

    file.write(output)

    if flush:
        file.flush()

helloWorld("print")
