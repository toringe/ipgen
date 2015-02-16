#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Core modules
import sys
import argparse
import random

# Third party modules
import ipaddr


def genvalidipv4():
    """ Generate a random valid IPv4 address, excluding all the
        reserved address blocks as specified in RFC 6890
    """
    invalid4 = ['0.0.0.0/8', '10.0.0.0/8', '100.64.0.0/10', '127.0.0.0/8',
                '169.254.0.0/16', '172.16.0.0/12', '192.0.0.0/24',
                '192.0.0.0/29', '192.0.2.0/24', '192.88.99.0/24',
                '192.168.0.0/16', '192.18.0.0/15', '198.51.100.0/24',
                '203.0.113.0/24', '240.0.0.0/4', '255.255.255.255/32']

    intip = random.getrandbits(32)

    for i in invalid4:
        if ipaddr.IPAddress(intip) in ipaddr.IPNetwork(i):
            intip = genvalidipv4()  # Regenerate the IP until it's valid

    return intip


def genvalidipv6():
    """ Generate a random valid IPv6 address, excluding all the
        reserved address blocks as specified in RFC 6890
    """
    invalid6 = ['::/128', '::1/128', '64:ff9b::/96', '::ffff:0:0/96',
                '100::/64', '2001::/23', '2001::/32', '2001:2::/48',
                '2001:db8::/32', '2001:10::/28', '2002::/16', 'fc00::/7',
                'fe80::/10']

    intip = random.getrandbits(128)

    for i in invalid6:
        if ipaddr.IPAddress(intip) in ipaddr.IPNetwork(i):
            intip = genvalidipv6()  # Regenerate the IP until it's valid

    return intip


def main():
    parser = argparse.ArgumentParser(description='Generate random IPs')
    parser.add_argument('-v4', action='store_true', help='Only generate IPv4')
    parser.add_argument('-v6', action='store_true', help='Only generate IPv6')
    parser.add_argument('num', type=int, help='Number of IPs to be generated')
    args = parser.parse_args()

    if args.v4:
        for _ in range(int(args.num)):
            print ipaddr.IPAddress(genvalidipv4())
    elif args.v6:
        for _ in range(int(args.num)):
            print ipaddr.IPAddress(genvalidipv6())
    else:
        for _ in range(int(args.num)):
            if random.random() < 0.5:  # Randomly generate both v4 and v6
                print ipaddr.IPAddress(genvalidipv4())
            else:
                print ipaddr.IPAddress(genvalidipv6())
    return 0

if __name__ == '__main__':
    status = main()
    sys.exit(status)
