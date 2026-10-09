
def commands(binary_str):
    actions = ["wink", "double blink", "close your eyes", "jump"]
    
    # Convert the binary string to an integer
    number = int(binary_str, 2)

    
    result = []

    for i, action in enumerate(actions):
        if number & (1 << i):
            result.append(action)

    
    if number & 16:
        result.reverse()

    return result

