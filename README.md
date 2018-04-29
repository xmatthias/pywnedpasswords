# pywnedPasswords

[![Build Status](https://travis-ci.org/xmatthias/pywnedpasswords.svg?branch=master)](https://travis-ci.org/xmatthias/pywnedpasswords)

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

or in case your password is secure

> Password to check:
> 
> Your password did not appear in PwnedPasswords yet.


### Passing the password as a command line argument

**Discouraged - as it might leaves the password in your shell history**

``` bash
pywnedpasswords Passw0rd
```

> Found your password 46980 times.


### Piping the password 

**Discouraged - as it might leaves the password in your shell history**

``` bash
echo -n 'Passw0rd!' | pywnedpasswords 
```

> Found your password 46980 times.

### Reading passwords from a file 


``` bash
pywnedpasswords -f list-of-passwords.txt
```

Result is in the form: `<line number>: <number of time the password was found>`. `0` meaning the password is not known from Have I Been Pwned yet.

> <pre>
> 0: 7026
> 1: 45337
> 2: 376
> 3: 51
> 4: 27
> 5: 11
> 6: 136
> 7: 1
> 8: 6
> 9: 1
> 10: 0
> 11: 0
> 12: 0
> </pre>



## Exit code

The `pywnedpasswords` exits with code `2` if the password is know of Have I Been Pwned already, and exit code `0` otherwise.

© xmatthias 2018
