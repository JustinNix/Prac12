"""
CP1404/CP5632 Practical
Testing demo using assert and doctest
"""

import doctest
from Car import Car


def repeat_string(s, n):
    """
    repeat string s, n times, with spaces in between
    """
    if n < 1:
        return 0
    repeat_string(s, n - 1)
    return " ".join([s]*n)


def is_long_word(word, length=5):
    """
    Determine if the word is as long or longer than the length passed in
    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    >>> is_long_word("Python", 6)
    True
    """
    return len(word) >= length


def format_phrase(phrase):
    """
    format a phrase as a sentence - starting with a capital and ending with a single full stop

    >>> format_phrase('hello')
    'Hello.'
    >>> format_phrase('It is an ex parrot.')
    'It is an ex parrot.'
    >>> format_phrase('This is correct.')
    'This is correct.'
    """
    if phrase[0].isupper() and phrase[-1] == '.':
        return phrase
    else:
        return "not a good phrase"

#phrase = format_phrase(input("enter a phrase: "))


def run_tests():
    # assert test with no message - used to see if the function works properly
    assert repeat_string("Python", 1) == "Python"
    # the test below should fail
    assert repeat_string("hi", 2) == "hi hi"

    # assert test with custom message - used to see if Car's init method sets the odometer correctly
    # this should pass (no output)
    test_car = Car()
    assert test_car.odometer == 0, "Car does not set odometer correctly"

    # TODO: 2. write assert statements to show if Car sets the fuel correctly
    # Note that Car's __init__ function sets the fuel in one of two ways: using the value passed in or the default
    # You should test both of these
    test_car = Car(fuel=10)
    assert test_car.fuel == 10, "Car does not set odometer correctly"
    test_car_default = Car()
    assert test_car_default.fuel == 0, "default not working "


#run_tests()

# TODO: 3. Uncomment the following line and run the doctests
doctest.testmod()

# TODO: 4. Fix the failing is_long_word function (don't change the tests, but the function!) - i dont understand what youre asking me to change? make it pass the test?

# TODO: 5. Write and test a function to format a phrase as a sentence - starting with a capital and ending with a single full stop
# Important: start with a function header and just use pass as the body
# then add doctests so that:
# 'hello' -> ''Hello.'
# 'It is an ex parrot.' -> 'It is an ex parrot.'
# and one more you decide (that's valid!)
# then write the body of the function so that the tests pass


