"""
General helper functions
"""

import re


def capitalize(s, exceptions):
    """
    This function will title case a string, skipping the list of exceptions.

    I pilfered this from the following stackoverflow.com link...

    https://stackoverflow.com/questions/3728655/titlecasing-a-string-with-exceptions
    """
    word_list = re.split(" ", s)  # re.split behaves as expected
    final = [word_list[0].capitalize()]
    for word in word_list[1:]:
        final.append(word if word in exceptions else word.capitalize())
    return " ".join(final)


def proper_case_list(list, articles=["a", "an", "of", "the", "is"]):
    return [capitalize(i, articles) for i in list]