import re

def normalize_math_text(text):

    text = text.lower()

    replacements = {
        "square root of": "sqrt",
        "squared": "^2",
        "cubed": "^3",
        "raised to the power": "^",
        "raised to": "^",
    }

    for phrase, symbol in replacements.items():
        text = text.replace(phrase, symbol)

    # Example cleanup
    text = re.sub(r"\s+", " ", text)

    return text.strip()