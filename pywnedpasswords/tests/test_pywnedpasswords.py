from unittest.mock import MagicMock
import pytest
from pywnedpasswords.pywnedpasswords import hashpass, known_count, check
# , check_from_file


from requests.models import Response


@pytest.fixture()
def mock_response():
    """ Mock response for Passw0rd!"""
    the_response = Response()
    the_response.status_code = 200
    the_response._content = b"""973E7B0BF9D160F9F60E3C3ACD2494BEB0D: 1286
00848DA0D98815071353DC300103B294EFE:1234"""
    return the_response


def test_hashpass():
    assert hashpass("Passw0rd!") == "F4A69973E7B0BF9D160F9F60E3C3ACD2494BEB0D"


def test_knowncount(mock_response, mocker):

    mocker.patch('pywnedpasswords.pywnedpasswords.s',
                 MagicMock(get=MagicMock(return_value=mock_response)))

    assert known_count('Passw0rd!') == 1286


def test_check(mock_response, mocker, capsys):
    mocker.patch('pywnedpasswords.pywnedpasswords.s',
                 MagicMock(get=MagicMock(return_value=mock_response)))
    assert check("Passw0rd!")
    captured = capsys.readouterr()
    assert captured.out == 'Found your password 1286 times.\n'
    assert not check("Passw0rd")
    captured = capsys.readouterr()
    assert captured.out == 'Your password did not appear in PwnedPasswords yet.\n'
