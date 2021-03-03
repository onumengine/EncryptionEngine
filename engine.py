from typing import Dict

encoding_data: Dict[str, int] = {
    "a": "z",
    "b": "y",
    "c": "x",
    "d": "w",
    "e": "v",
    "f": "u",
    "g": "t",
    "h": "s",
    "i": "r",
    "j": "q",
    "k": "p",
    "l": "o",
    "m": "n",
    "n": "m",
    "o": "l",
    "p": "k",
    "q": "j",
    "r": "i",
    "s": "h",
    "t": "g",
    "u": "f",
    "v": "e",
    "w": "d",
    "x": "c",
    "y": "b",
    "z": "a"
}

def encode_string(text: str) -> str:
    length: int = len(text);
    for i in range(length):
        current_letter = text[i]
        if current_letter in encoding_data:
            text.replace(current_letter, encoding_data[current_letter])
        elif current_letter.lower() in encoding_data:
            text.replace(current_letter, encoding_data[current_letter.lower()].upper())
        else:
            print("encoding failed")