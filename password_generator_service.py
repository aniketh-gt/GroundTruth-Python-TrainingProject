import random

def pass_gen(pass_dict):
    DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                         'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                         'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                         'z']
    UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                         'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q',
                         'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                         'Z']
    SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
               '*', '(', ')', '<']

    password = ""
    
    max_len = pass_dict['length_of_password']
    lc_len = pass_dict['length_of_lowercase']
    uc_len= pass_dict['length_of_uppercase']
    dig_len = pass_dict['length_of_number']
    symbol_len = pass_dict['length_of_special_character']
    
    if max_len >= (lc_len + uc_len + dig_len + symbol_len):
        for i in range(lc_len):
            rand_lower = random.choice(LOCASE_CHARACTERS)
            password += rand_lower

        for i in range(uc_len):
            rand_upper = random.choice(UPCASE_CHARACTERS)
            password += rand_upper

        for i in range(dig_len):
            rand_dig = random.choice(DIGITS)
            password += rand_dig

        for i in range(symbol_len):
            rand_symbols = random.choice(SYMBOLS)
            password += rand_symbols

        p_list = list(password)
        random.shuffle(p_list)

        password = "".join(p_list)

        return password
    return "Condition Mismatch"
