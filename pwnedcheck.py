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
from hashlib import sha1
from getpass import getpass
from requests import get


API_URL = "https://api.pwnedpasswords.com/range/{}"


def hashpass():
    """ Function to return password hash
        The password is requested using the hashlib.getpass function.
        The password will not be visible during insertion.
    """
    return sha1(getpass("Password to check: ").encode("utf-8")
                ).hexdigest().upper()


def main():
    print("Welcome to PywnedPasswords")
    print("Your password will not be transmitted over the network!")

    passhash = hashpass()
    ph_short = passhash[:5]
    req = get(API_URL.format(ph_short))
    passl = req.text
    for l in passl.split('\n'):
        larr = l.split(":")
        rhash = larr[0]
        if ph_short + rhash == passhash:
            print("Found your password {} times.".format(larr[1].strip()))
            return
    print("Your password did not appear in PwnedPasswords yet.")


if __name__ == "__main__":
    main()
