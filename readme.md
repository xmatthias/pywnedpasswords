# pywnedPasswords

This script uses the pwnedpasswords.com v2 api to check your password in
a secure way (using the [K-anonymity](https://en.wikipedia.org/wiki/K-anonymity) method)

The full Hash is never transmitted over the wire, only the first 5 characters.
The comparison happens offline.

Special thanks to Troy Hunt ([@troyhunt](https://twitter.com/troyhunt)) for making this script possible.

© Xmatthias 2018
