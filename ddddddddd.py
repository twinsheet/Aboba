import random as r
import string as s


def generate_password(length=8, use_uppercase=True, use_lowercase=True, use_digits=True, use_special=True):
    characters = ' '
    if use_uppercase:
        characters += s.ascii_uppercase
    if use_lowercase:
        characters += s.ascii_lowercase
    if use_digits:
        characters += s.digits
    if use_special:
        characters += s.punctuation

    if not characters:
        raise ValueError('')