from encoding_data import string_map

def get_encoded_string(text):

    temp_string = ""

    for letter in text:
        current_letter = letter
        if current_letter in string_map:
            temp_string += (string_map[current_letter])
        elif current_letter.lower() in string_map:
            temp_string += (string_map[current_letter.lower()].upper())
        elif current_letter == " ":
            temp_string += ("_")
        else:
            continue
    
    encoded_string = temp_string.replace("'", "").replace(",", "").replace("[", "").replace("]", "").replace(" ", "").replace("_", " ")
    return encoded_string

def run_script():
    unencoded_string = input("Enter a string: ")
    encoded_string = get_encoded_string(unencoded_string)
    print(encoded_string)


run_script()