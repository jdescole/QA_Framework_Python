import pytest
import datetime


@pytest.fixture()
def ordered_array():
    an_array = [-5, -20, 5, -23, 0, 23, -6, 23, 67, 4324, -3213, 444]
    ordered_array = []
    while an_array:
        _min = an_array[0]
        for nmbr in an_array:
            if nmbr < _min:
                _min = nmbr
        ordered_array.append(_min)
        an_array.remove(_min)
    return ordered_array


def test_a_way_to_reverse(ordered_array):
    a_lenght = len(ordered_array)
    inv_array = []
    a_lenght -= 1
    for e in range(a_lenght):
        inv_array.append(ordered_array[a_lenght])
        a_lenght -= 1
    print(inv_array)
    print(ordered_array)


def test_another_way_to_do_this(ordered_array):
    a_lenght = len(ordered_array)
    for i in range(int(a_lenght / 2)):
        n = ordered_array[i]
        ordered_array[i] = ordered_array[a_lenght - i - 1]
        ordered_array[a_lenght - i - 1] = n
    print(ordered_array)

