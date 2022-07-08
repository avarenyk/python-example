import pytest
from app.conditional_operator.max import max


@pytest.mark.parametrize(
    'first, second, answer',
    [
        (1, 2, 2),
        (10, 30, 30),
        (-10, 2, 2),
        (5, 5, 'a equal b'),
    ]
)
def test_plus(first: int, second: int, answer: int):
    assert answer == max(first, second)


def test_plus_exception():
    with pytest.raises(TypeError):
        max(10, 's')
    with pytest.raises(TypeError):
        max('asd', 2)
    with pytest.raises(TypeError):
        max(10.2, 2)
