from del3 import count_vowels


def test_no_vowels():
    assert count_vowels("qwrt") == 0
    assert count_vowels("Tt") == 0
    assert count_vowels("123 123") == 0
    assert count_vowels("") == 0

def test_all_vowels_from_swedish_alphabet():
    assert count_vowels("aqwrt") == 1
    assert count_vowels("Tet") == 1
    assert count_vowels("123 123i") == 1
    assert count_vowels("o") == 1
    assert count_vowels("gutr") == 1
    assert count_vowels("y877") == 1
    assert count_vowels("åäö") == 3




count_vowels("aeiouyåäö")