ipgen
=====

Generate lists of psudo-random valid IP addresses. Valid in the sense that all address blocks as defined in [RFC 6890](http://tools.ietf.org/html/rfc6890) are excluded. Supports both IPv4 and IPv6.

Usage
-----
```
ipgen.py [-h] [-v4] [-v6] num

positional arguments:
   num         Number of IPs to be generated

optional arguments:
  -h, --help  show this help message and exit
  -v4         Only generate IPv4
  -v6         Only generate IPv6
```

Examples
--------

Generate one hundred addresses, with a mix of v4 and v6.

```ipgen 100```

Generate fifty thousand IPv4 addresses

```ipgen.py -v4 50000```
  
