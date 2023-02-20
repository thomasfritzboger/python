def remove_e(word):
    if isinstance(word, str):
        return word.replace("e", "")
    else: return AttributeError("The input is not a string")