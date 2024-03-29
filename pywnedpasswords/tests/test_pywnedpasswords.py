import io
from unittest.mock import MagicMock

import pytest
from requests.models import Response

from pywnedpasswords.pywnedpasswords import (
    check,
    check_from_file,
    hashpass,
    known_count,
    main_flow,
)


@pytest.fixture()
def mock_response():
    """Mock response for Passw0rd!"""
    the_response = Response()
    the_response.status_code = 200
    the_response._content = b"""973E7B0BF9D160F9F60E3C3ACD2494BEB0D: 1286
943B1609FFFBFC51AAD666D0A04ADF83C9D:1234"""
    return the_response


def test_hashpass():
    assert hashpass("Passw0rd!") == "F4A69973E7B0BF9D160F9F60E3C3ACD2494BEB0D"
    assert hashpass("Password") == "8BE3C943B1609FFFBFC51AAD666D0A04ADF83C9D"


def test_knowncount(mock_response, mocker):
    mocker.patch(
        "pywnedpasswords.pywnedpasswords.s", MagicMock(get=MagicMock(return_value=mock_response))
    )

    assert known_count("Passw0rd!") == 1286


def test_check(mock_response, mocker, capsys):
    mocker.patch(
        "pywnedpasswords.pywnedpasswords.s", MagicMock(get=MagicMock(return_value=mock_response))
    )
    assert check("Passw0rd!")
    captured = capsys.readouterr()
    assert captured.out == "Found your password 1286 times.\n"
    assert not check("Passw0rd")
    captured = capsys.readouterr()
    assert captured.out == "Your password did not appear in PwnedPasswords yet.\n"


def test_check_from_file(mock_response, mocker, capsys):
    mocker.patch(
        "pywnedpasswords.pywnedpasswords.s", MagicMock(get=MagicMock(return_value=mock_response))
    )
    assert check_from_file("pywnedpasswords/tests/test_pass.txt") == 2
    captured = capsys.readouterr()
    assert captured.out == "0: 1286\n1: 1234\n2: 0\n"


def test_check_test_from_file_error(mock_response, mocker):
    mocker.patch(
        "pywnedpasswords.pywnedpasswords.s", MagicMock(get=MagicMock(return_value=mock_response))
    )
    assert check_from_file("pywnedpasswords/tests/test_pass11.txt") == 1
    # Check with not finding passwords -
    # relies on mock-response to not contain any of these passwords
    assert check_from_file("pywnedpasswords/tests/test_pass_nofind.txt") == 0


def test_main_flow(mocker, monkeypatch):
    check_mock = mocker.patch("pywnedpasswords.pywnedpasswords.check", return_value=True)
    getpass_mock = mocker.patch(
        "pywnedpasswords.pywnedpasswords.getpass", return_value="Passw0rd!"
    )

    with pytest.raises(SystemExit) as wrapped_e:
        main_flow(["xx", "Passw0rd!"])
        assert wrapped_e.value.code == 0

    assert getpass_mock.call_count == 0
    assert check_mock.call_count == 1
    check_mock.reset_mock()

    with pytest.raises(SystemExit) as wrapped_e:
        main_flow(["xx", "-f", "pywnedpasswords/tests/test_pass11.txt"])
        assert wrapped_e.value.code == 0

    assert getpass_mock.call_count == 0
    # calls check_from_file
    assert check_mock.call_count == 0

    mocker.patch("pywnedpasswords.pywnedpasswords.sys.stdin.isatty", return_value=True)

    main_flow(["xx"])

    assert getpass_mock.call_count == 1
    assert check_mock.call_count == 1

    getpass_mock.reset_mock()
    check_mock.reset_mock()

    # Test Piping
    monkeypatch.setattr("pywnedpasswords.pywnedpasswords.sys.stdin", io.StringIO("my input"))
    with pytest.raises(SystemExit) as wrapped_e:
        main_flow(["xx"])
        assert wrapped_e.value.code == 0

    assert getpass_mock.call_count == 0
    assert check_mock.call_count == 1
