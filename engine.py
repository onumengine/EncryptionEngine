encoding_data = {
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

def get_encoded_string(text):

    length = len(text)
    string_array = []

    for i in range(length):
        current_letter = text[i]
        if current_letter in encoding_data:
            string_array.append(encoding_data[current_letter])
        elif current_letter.lower() in encoding_data:
            string_array.append(encoding_data[current_letter.lower()].upper())
        elif current_letter == " ":
            string_array.append("_")
        else:
            continue
    
    new_string = str(string_array)
    refined_string = new_string.replace("'", "").replace(",", "").replace("[", "").replace("]", "").replace(" ", "").replace("_", " ")
    return refined_string

def run_script():
    unencoded_string = input("Enter a string: ")
    encoded_string = get_encoded_string(unencoded_string)
    print(encoded_string)


run_script()