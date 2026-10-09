
def find_anagrams(word, candidates):
    result = []
    target = word.lower()

    for candidate in candidates:
        candidate_lower = candidate.lower()

        if candidate_lower == target:
            continue
            
        if sorted(candidate_lower) == sorted(target):
            result.append(candidate)

    return result

