from challenges.difficult.Challenge_1.solution import guess_number


def test_guess_number(capsys, mocker):
    m = mocker.MagicMock(side_effect=['correct', 'correct', 'correct'])
    mocker.patch('builtins.input', new=m)
    captured = capsys.readouterr()

    for _ in range(3):
        guess_number()
        if captured.out != '':
            with capsys.disabled():
                assert 'Is your number' == captured.out[:-3]
                print(captured.out[:-3])
