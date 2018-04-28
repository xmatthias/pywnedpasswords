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
from hashlib import sha1
from getpass import getpass
from requests import get


API_URL = "https://api.pwnedpasswords.com/range/{}"


def hashpass(password):
    """ Function to return password hash"""
    return sha1(password.encode("utf-8")).hexdigest().upper()


def check(password):
    passhash = hashpass(password)
    ph_short = passhash[:5]
    req = get(API_URL.format(ph_short))
    pywnedpasswords = req.text
    for l in pywnedpasswords.split('\n'):
        larr = l.split(":")
        rhash = larr[0]
        if ph_short + rhash == passhash:
            print("Found your password {} times.".format(larr[1].strip()))
            sys.exit(2)
    print("Your password did not appear in PwnedPasswords yet.")
    sys.exit(0)


def main():
    if len(sys.argv) == 2:
        password = str(sys.argv[1])
        check(password)

    if not sys.stdin.isatty():
        stdin_text = sys.stdin.read()
        if len(stdin_text):
            check(stdin_text)


    print("Welcome to PywnedPasswords")
    print("Your password will not be transmitted over the network!")
    print()
    # The password is requested using the hashlib.getpass function.
    # The password will not be visible during insertion.
    check(getpass("Password to check: "))


if __name__ == "__main__":
    main()

