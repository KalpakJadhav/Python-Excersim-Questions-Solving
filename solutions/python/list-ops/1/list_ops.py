def append(list1, list2):
    # Create a new list containing all elements of list1 followed by list2
    result = []
    for item in list1:
        result = result + [item]  # Building manually without list.append()
    for item in list2:
        result = result + [item]
    return result


def concat(lists):
    # Flatten a list of lists into a single list
    result = []
    for sublist in lists:
        result = append(result, sublist)
    return result


def filter(function, list):
    # Return items where function(item) evaluates to True
    result = []
    for item in list:
        if function(item):
            result = result + [item]
    return result


def length(list):
    # Count the total number of items
    count = 0
    for _ in list:
        count += 1
    return count


def map(function, list):
    # Apply a function to every item in the list
    result = []
    for item in list:
        result = result + [function(item)]
    return result


def foldl(function, list, initial):
    # Reduce from left to right: function(accumulator, item)
    accumulator = initial
    for item in list:
        accumulator = function(accumulator, item)
    return accumulator


def foldr(function, list, initial):
    # Reduce from right to left: function(accumulator, item)
    accumulator = initial
    # Walk backwards using reverse to avoid built-ins
    for item in reverse(list):
        accumulator = function(accumulator, item)
    return accumulator


def reverse(list):
    # Return a new list with elements in reverse order
    result = []
    for item in list:
        result = [item] + result
    return result
