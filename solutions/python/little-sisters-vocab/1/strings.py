"""Functions for creating, transforming, and adding prefixes to strings."""


def add_prefix_un(word):
    """Take the given word and add the 'un' prefix.

    Parameters:
        word (str): The root word.

    Returns:
        str: Root word prepended with 'un'.
    """
    return "un" + word


def make_word_groups(vocab_words):
    """Transform a list containing a prefix and words.

    Parameters:
        vocab_words (list[str]): Vocabulary words with prefix at first index.

    Returns:
        str: Prefix followed by vocabulary words with prefix applied.
    """
    prefix = vocab_words[0]
    words_with_prefix = [prefix + word for word in vocab_words[1:]]
    return " :: ".join([prefix] + words_with_prefix)


def remove_suffix_ness(word):
    """Remove the suffix from the word while keeping spelling in mind.

    Parameters:
        word (str): Word to remove suffix from.

    Returns:
        str: Word with suffix removed & spelling adjusted.
    """
    stem = word[:-4]  # removes 'ness'
    if stem.endswith("i"):
        return stem[:-1] + "y"
    return stem


def adjective_to_verb(sentence, index):
    """Change the adjective within the sentence to a verb.

    Parameters:
        sentence (str): The word used in a sentence as an adjective.
        index (int): Index of the adjective to remove and transform.

    Returns:
        str: The extracted adjective in verb form.
    """
    words = sentence.split()
    adjective = words[index].strip(".,?!")
    return adjective + "en"