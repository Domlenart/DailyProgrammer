from .solution import get_user_data


def test_answer(mocker):
    m = mocker.MagicMock(side_effect=['X', '25', 'Y'])
    mocker.patch('builtins.input', new=m)
    data = get_user_data(log=False)
    assert data == 'Your name is X, you are 25 years old, and your username is Y'

