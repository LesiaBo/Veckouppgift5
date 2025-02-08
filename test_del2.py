# Det har smugit sig in kommentarer i stället för kod på några ställen. Skriv färdigt testfallen
# test_empty_list och test_number_list.

# Returnerar summan av alla tal i listan
def sum_list(list):
    return sum(list)


def test_empty_list():
    expected = 0
    actual = sum_list([]) 
    assert actual == expected

def test_number_list():
    assert sum_list([5]) == 5 # 1 element in a list
    assert sum_list([1, 2, 3]) == 6  # 1 + 2 + 3 = 6
    assert sum_list([-1, -2, -3]) == -6  # Negativa numbers
    assert sum_list([10, 20, 30, 40]) == 100  # bigger numbers