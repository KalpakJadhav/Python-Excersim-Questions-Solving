def transform(legacy_data):
    """
    Transforms the legacy point-to-letters mapping into a 
    one-to-one letter-to-point mapping with lowercase letters.
    """
    return {
        letter.lower(): points
        for points, letters in legacy_data.items()
        for letter in letters
    }
