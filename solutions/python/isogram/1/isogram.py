def is_isogram(phrase):
    """Return True if no letter appears more than once."""
    letters = [
        char.lower()
        for char in phrase
        if char.isalpha()
    ]

    return len(letters) == len(set(letters))