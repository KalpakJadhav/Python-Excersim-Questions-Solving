"""Functions for organizing and calculating student exam scores."""


def round_scores(student_scores):
    """Round all provided student scores."""
    result = []

    for score in student_scores:
        result.append(round(score))

    return result


def count_failed_students(student_scores):
    """Count the number of failing students."""
    count = 0

    for score in student_scores:
        if score <= 40:
            count += 1

    return count


def above_threshold(student_scores, threshold):
    """Return scores at or above the threshold."""
    result = []

    for score in student_scores:
        if score >= threshold:
            result.append(score)

    return result


def letter_grades(highest):
    """Create grade thresholds."""
    step = (highest - 40) // 4

    return [41, 41 + step, 41 + step * 2, 41 + step * 3]


def student_ranking(student_scores, student_names):
    """Create student ranking."""
    result = []

    for i in range(len(student_scores)):
        result.append(str(i + 1) + ". " + student_names[i] + ": " + str(student_scores[i]))

    return result


def perfect_score(student_info):
    """Find the first student with a perfect score."""
    for student in student_info:
        if student[1] == 100:
            return student

    return []