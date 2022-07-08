import pytest
from app.conditional_operator.chess import chess


@pytest.mark.parametrize(
    'x1, y1, x2, y2, answer',
    [
        ('a', 5, 'b', 2, 'No'),
        ('c', 1, 'c', 2, 'Yes'),
        ('a', 3, 'b', 8, 'No'),
        ('a', 1, 'b', 2, 'No'),
        ('h', 1, 'h', 2, 'Yes'),
    ]
)
def test_chess(x1:str, y1:int, x2:str, y2:int, answer: str):
    assert answer == chess(x1, y1, x2, y2)


def test_year_exception():
    with pytest.raises(TypeError):
        chess('h', 'h', 'h', '2')
    with pytest.raises(TypeError):
        chess(1, 'h', 2, '2')
    with pytest.raises(ValueError):
        chess('h', 11, 'h', 2)
    with pytest.raises(ValueError):
        chess('hw', 1, 'h', 2)
    with pytest.raises(ValueError):
        chess('k', 1, 'h', 25)
    with pytest.raises(ValueError):
        chess('h', 1, 'h', 25)
    with pytest.raises(ValueError):
        chess('h', 21, 'h', 5)
