import pytest
from app.conditional_operator.year import year


@pytest.mark.parametrize(
    'years, answer',
    [
        (1, 'No'),
        (4, 'Yes'),
        (200, 'No'),
        (2000, 'Yes'),
    ]
)
def test_year(years: int, answer: str):
    assert answer == year(years)


def test_year_exception():
    with pytest.raises(TypeError):
        year('s')
    with pytest.raises(TypeError):
        year('')
    with pytest.raises(TypeError):
        year('100')
    with pytest.raises(ValueError):
        year(-10)
    with pytest.raises(ValueError):
        year(0)
    with pytest.raises(TypeError):
        year(10.2)
