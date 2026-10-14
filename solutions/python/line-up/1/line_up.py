# Change the function name to match what the test file is trying to import
def line_up(name: str, number: int) -> str:
    last_two_digits = number % 100
    last_digit = number % 10
    
    if last_two_digits in {11, 12, 13}:
        suffix = "th"
    elif last_digit == 1:
        suffix = "st"
    elif last_digit == 2:
        suffix = "nd"
    elif last_digit == 3:
        suffix = "rd"
    else:
        suffix = "th"
        
    noun = "customer"
    
    return f"{name}, you are the {number}{suffix} {noun} we serve today. Thank you!"
