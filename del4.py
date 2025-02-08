#4 Formulera testfall för en funktion som hittar största talet i en lista.
# Returnerar det största talet i listan
# Returnerar None om det inte finns något
#def find_max(list):

#test1: empty list->return None
#test2: list doesn't contain numbers, but other digit types->return 0
#test3: list of same numbers->any of them
#test4: list 1, 2, 9999, 200 ->9999
#test5: list -8888, 5, 0, 2
#rest6: list of letters and numbers a, r, (, 34 ->34

def find_max(my_list):
    temp_max = -9999999999
    if len(my_list) == 0:
        return None
    else:
        for i in range(len(my_list)):
            if isinstance(my_list[i], (int, float)) and  my_list[i] > temp_max:
                temp_max = my_list[i]
        if temp_max == -9999999999:
            return 0
        else:
            return temp_max