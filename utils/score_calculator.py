def calculate_score(value, maximum):

    if maximum == 0:
        return 0

    return round((value / maximum) * 100)