# 5 Winner takes it all brukar det ju heta, men nu ska vi försöka ge lite heder åt alla andrapristagare.
# Formulera testfall för en funktion som hittar näst största talet i en lista!
# Returnerar det nästa största talet i listan
# Returnerar None om det inte finns något
# Om det är delad förstaplats så returneras det talet

def find_2nd_max(my_list):
    if not my_list:
        return None  # Handle empty list

    temp_max = float('-inf')
    temp_second_max = float('-inf')

    for num in my_list:
        if isinstance(num, (int, float)):  # Ensure number type
            if num > temp_max:
                temp_second_max = temp_max
                temp_max = num
            elif temp_max > num > temp_second_max:
                temp_second_max = num

    return temp_max if temp_second_max == float('-inf') else temp_second_max
