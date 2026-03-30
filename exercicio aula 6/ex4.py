def solution(text, ending):
    numero_len = len(text)
    numero_ending = len(ending)
    resultado = numero_len - numero_ending

    if isinstance(text, str) and text[resultado:numero_len] == ending:
        return True
    else:
        return False