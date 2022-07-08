import pytest
from app.conditional_operator.icecream import icecream


@pytest.mark.parametrize(
    'quantity, answer',
    [
        (1, 'No'),
        (4, 'No'),
        (3, 'Yes'),
        (5, 'Yes'),
        (7, 'No'),
        (33, 'No')
    ]
)
def test_icecream(quantity: int, answer: str):
    assert answer == icecream(quantity)


def test_year_exception():
    with pytest.raises(TypeError):
        icecream('s')
    with pytest.raises(TypeError):
        icecream('')
    with pytest.raises(TypeError):
        icecream('100')
    with pytest.raises(ValueError):
        icecream(-10)
    with pytest.raises(ValueError):
        icecream(0)
    with pytest.raises(TypeError):
        icecream(10.2)
