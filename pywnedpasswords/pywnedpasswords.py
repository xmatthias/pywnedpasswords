#!/usr/sbin/env python3
"""
This script uses the pwnedpasswords.com v2 api to check your password in
a secure way (using the K-anonymity method)
https://en.wikipedia.org/wiki/K-anonymity

The full Hash is never transmitted over the wire, only the first 5 characters.
The comparison happens offline.

Special thanks to Troy Hunt (@troyhunt) for making this script possible.

© Xmatthias 2018
"""
import sys
import fileinput
from hashlib import sha1
from getpass import getpass
from requests import Session

# Version number - single source of truth for this value
__version__ = "0.5"


API_URL = "https://api.pwnedpasswords.com/range/{}"
s = Session()
s.headers = {"User-Agent": "pywnedpasswords/{}".format(__version__)}


def hashpass(password: str) -> str:
    """ Function to return password hash"""
    return sha1(password.encode("utf-8")).hexdigest().upper()


def known_count(password: str) -> int:
    """ Return the number of time the password was found in breaches """
    passhash = hashpass(password)
    ph_short = passhash[:5]
    req = s.get(API_URL.format(ph_short))
    pywnedpasswords = req.text
    for l in pywnedpasswords.split('\n'):
        larr = l.split(":")
        rhash = larr[0]
        if ph_short + rhash == passhash:
            return int(larr[1].strip())
    return 0


def check(password: str) -> bool:
    count = known_count(password)
    if count > 0:
        print("Found your password {} times.".format(count))
        return True
    else:
        print("Your password did not appear in PwnedPasswords yet.")
        return False


def check_from_file(filepath):
    breach_found = False
    try:
        for line_number, line in enumerate(fileinput.input([filepath])):
            password = line[:-1] if line[-1] == '\n' else line
            count = known_count(password)
            if count > 0:
                breach_found = True
            print("{}: {}".format(line_number, count))
    except FileNotFoundError as err:
        print(err)
        sys.exit(1)
    except KeyboardInterrupt:
        sys.exit(1)

    if breach_found:
        sys.exit(2)
    else:
        sys.exit(0)


def main():
    if len(sys.argv) == 2:
        password = str(sys.argv[1])
        sys.exit(2 if check(password) else 0)

    if len(sys.argv) == 3 and sys.argv[1] == '-f':
        check_from_file(sys.argv[2])

    if not sys.stdin.isatty():
        stdin_text = sys.stdin.read()
        if len(stdin_text):
            sys.exit(2 if check(stdin_text) else 0)

    print("Welcome to PywnedPasswords")
    print("Your password will not be transmitted over the network!")
    print()
    # The password is requested using the hashlib.getpass function.
    # The password will not be visible during insertion.
    try:
        check(getpass("Password to check: "))
    except KeyboardInterrupt:
        sys.exit(1)


if __name__ == "__main__":
    main()
