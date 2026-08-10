def validate_text(text):

    if text.strip() == "":
        return False

    return True


def validate_url(url):

    if url.startswith("http://") or url.startswith("https://"):
        return True

    return False