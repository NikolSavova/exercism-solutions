def response(hey_bob):
    text = hey_bob.strip()
    question = text.endswith("?")
    yelling = text.isupper()

    if not text:
        return "Fine. Be that way!"
    if yelling and question:
        return "Calm down, I know what I'm doing!"
    if yelling:
        return "Whoa, chill out!"
    if question:
        return "Sure."
    return "Whatever."
