def is_pangram(sentence):
    """Return True if the sentence contains every letter of the alphabet."""
    return set("abcdefghijklmnopqrstuvwxyz").issubset(sentence.lower())
