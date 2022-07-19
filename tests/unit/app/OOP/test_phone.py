import pytest
from app.OOP.phone import Phone


@pytest.mark.parametrize(
    'number, answer',
    [
        (Phone('099505095', 'Nokia 88', '100 gram'), '099505095'),
        (Phone('+38099505050', 'LG', '1000 gram'), '+38099505050'),
    ]
)
def test_get_number(number: str, answer: str):
    assert answer == Phone.getNumber(number)


@pytest.mark.parametrize(
    'answer, numbers',
    [
        ('123456, 5',
         ['self', 123456, 5]),
        ('8800553535, 12473670, +309999950',
         ['self', 8800553535, 12473670, '+309999950']),
        ('123456, 12473670, +309999950',
         ['self', 123456, 12473670, '+309999950']),
    ]
)
def test_sendMessage(answer, numbers):
    assert answer == Phone.sendMessage(*numbers)


@pytest.mark.parametrize(
    'answer, args',
    [
        (f'{"Petro"} is calling, number is {5}',
         ['self', '5', 'Petro']),
        (f'{"+38099505050"} is calling',
         ['self', "+38099505050"]),
    ]
)
def test_receiveCall(answer, args):
    assert answer == Phone.receiveCall(*args)


def test_Phone():
    with pytest.raises(TypeError):
        Phone('380099a059', 'iPhone 88', '100 gram')

    with pytest.raises(TypeError):
        Phone.sendMessage('self', 'gram')

    with pytest.raises(TypeError):
        Phone.sendMessage('self', 'Petro', '380099a059')
        Phone.sendMessage('self', '380099a059')
