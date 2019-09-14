from guessTheNumber import matchValue
def test_number_match():
    assert matchValue(10, 10) == 0 , "Should be 0"

def test_number_less_than():
    assert matchValue(10, 0) == 1 , "Should be 1"

def test_number_greater_than():
    assert matchValue(10, 200) == 1 , "Should be 1"

def test_number_not_matched():
    assert matchValue(10, 11) == 2 , "Should be 2"

def test_user_quit():
    assert matchValue(10,'q') == -1 , "Should be -1"

def test_invalid_input():
    assert matchValue(10, 'a') == 3 , "Should be 3"

if __name__ == "__main__":
    test_number_match()
    test_number_not_matched()
    test_number_less_than()
    test_number_greater_than()
    test_user_quit()
    test_invalid_input()
    print("Everything passed")