def input_service():
    default_auto_password = input("Enter 1 for customizing password or 2 for default generation")
    option = ["1","2"]
    while default_auto_password not in option:
        default_auto_password = input("Enter 1 for customizing password or 2 for default generation")
        if default_auto_password != "1" or default_auto_password != "2":
            print("Please choose 1 or 2")
    if default_auto_password == "2":
        return {"default_auto_password" : True, "length_of_password" : 16, "length_of_uppercase" : 4,"length_of_lowercase" : 4, "length_of_number" : 4, "length_of_special_character" : 4}
    match = False
    while not match:
        length_of_password = int(input("Enter the length of password"))
        length_of_uppercase = int(input("Enter the length of uppercase"))
        length_of_lowercase = int(input("Enter the length of lowercase"))
        length_of_number = int(input("Enter the length of number"))
        length_of_special_character = int(input("Enter the length of special character"))
        if length_of_password != length_of_uppercase + length_of_lowercase + length_of_number + length_of_special_character:
            print("Please Enter length of password = length of uppercase + length of lowercase + length of number + length of special character")
        else:
            return {"default_auto_password" : False, "length_of_password" : length_of_password, "length_of_uppercase" : length_of_uppercase,"length_of_lowercase" : length_of_lowercase, "length_of_number" : length_of_number, "length_of_special_character" : length_of_special_character}