import pytest
from app.lists.sort import sort


@pytest.mark.parametrize(
    'list, answer',
    [
        ([2, 1, 2], [1, 2, 2]),
        ([10, 15, 3], [3, 10, 15]),
        ([-10, 2, 8, 99, 18], [-10, 2, 8, 18, 99]),
    ]
)


def test_sort(list, answer):
    assert answer == sort(*list)


def test_plus_exception():
    with pytest.raises(TypeError):
        sort(10, 's')
    with pytest.raises(TypeError):
        sort('asd', 2)
    with pytest.raises(TypeError):
        sort('1', '2')
