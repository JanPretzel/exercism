import re

ALPHA_COUNT = 26


def is_pangram(text):
    clean = re.sub('[^a-z]+', '', text, flags=re.IGNORECASE)
    return len(list(set(clean.lower()))) == 26
