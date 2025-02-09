from del4 import find_max


#test1: []]->return None
#test2: list doesn't contain numbers, but other digit types->return 0
#test3: list of same numbers->any of them
#test4: list 1, 2, 9999, 200 ->9999
#test5: list -8888, 5, 0, 2
#rest6: list of letters and numbers a, r, (, 34 ->34

def test_empty_list():
    expected = None
    actual = find_max([])
    assert actual == expected

def test_no_numbers_in_list():
    assert find_max(["r","#","=?"]) == 0

def test_list_of_same_numbers():
    assert find_max([23, 23, 23])

def test_positive_numbers():
    assert find_max([1,2,9999,200])

def test_negative_numbers():
    assert find_max([-8888, 5, 0, 2])

def test_mix_of_data():
    assert find_max(["a", "r", "(", 34])