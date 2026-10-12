def is_iterable(thing):
    try:
        iter(thing)
    except TypeError:
        return False
    else:
        return True


def flatten(iterable):
    """Flatten a list of lists and exclude None/null values."""
    flattened = []
    for item in iterable:
        if is_iterable(item) and not isinstance(item, (str, bytes)):
            flattened.extend(flatten(item))
        elif item is not None:
            flattened.append(item)
    return flattened
