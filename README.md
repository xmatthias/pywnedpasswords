# pywnedPasswords

This script uses the pwnedpasswords.com v2 api to check your password in
a secure way (using the [K-anonymity](https://en.wikipedia.org/wiki/K-anonymity) method)

The full Hash is never transmitted over the wire, only the first 5 characters.
The comparison happens offline.

Special thanks to Troy Hunt ([@troyhunt](https://twitter.com/troyhunt)) for making this script possible.

## Installation

``` bash
pip install pywnedpasswords
```

## Usage

### Interactive 

``` bash
pywnedpasswords
```

Insert your password when asked.

the output will either be:

> Password to check:
> 
> Found your password 47205 times.

or in case your password is not secure

> Password to check:
> 
> Your password did not appear in PwnedPasswords yet.


### Passing the password as a command line argument


``` bash
pywnedpasswords Passw0rd
```

> Found your password 46980 times.


### Piping the password 


``` bash
echo -n 'Passw0rd!' | pywnedpasswords 
```

> Found your password 46980 times.


## Exit code

The `pywnedpasswords` exits with code `2` if the password is know of Have I Been Pwned already, and exit code `0` otherwise.

© xmatthias 2018
