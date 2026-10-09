def response(hey_bob):
    # Remove leading and trailing whitespace to check for silence
    message = hey_bob.strip()
    
    # Silence (empty string after stripping whitespace)
    if not message:
        return "Fine. Be that way!"
    
    # Check properties of the message
    is_question = message.endswith("?")
    is_yelling = message.isupper()
    
    # Yelling a question
    if is_yelling and is_question:
        return "Calm down, I know what I'm doing!"
    
    # Yelling (all caps, and contains at least one letter)
    if is_yelling:
        return "Whoa, chill out!"
    
    # Asking a question
    if is_question:
        return "Sure."
    
    # Default response for everything else
    return "Whatever."