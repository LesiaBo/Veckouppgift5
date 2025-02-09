from del5 import find_2nd_max
# test1:[]->return None
# test2: [444]-> 444
# test3: [23, -654, "fj", "/()#", 45] -> 23
# test4: [34, 57,2,45,57]-> 57

def test_empty_list():
    expected = None
    actual = find_2nd_max([])
    assert actual == expected

def test_one_nuber_in_list():
    assert find_2nd_max([444]) == 444

def test_positive_mix_of_data_containing_more_than_2_numbers():
    assert find_2nd_max([23, -654, "fj", "/()#", 45]) == 23

def test_positive_same_2_biggest_numbers():
    assert find_2nd_max( [5, 5, 5]) == 5


