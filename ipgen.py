#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import argparse
import random
import ipaddr


def genvalidip():
    """ Generate a random valid IPv4 address, excluding all the reserved
        address blocks as specified in RFC 6890
    """

    invalid = [	"0.0.0.0/8", "10.0.0.0/8", "100.64.0.0/10", "127.0.0.0/8",
                "169.254.0.0/16", "172.16.0.0/12", "192.0.0.0/24",
                "192.0.0.0/29", "192.0.2.0/24", "192.88.99.0/24",
                "192.168.0.0/16", "192.18.0.0/15", "198.51.100.0/24",
                "203.0.113.0/24", "240.0.0.0/4", "255.255.255.255/32"]

    intip = random.getrandbits(32)

    for i in invalid:
        if ipaddr.IPAddress(intip) in ipaddr.IPNetwork(i):
            intip = genvalidip()  # Regenerate the IP until it's valid

    return intip


def main():
    parser = argparse.ArgumentParser(description='Generate random IPs')
    parser.add_argument("num", type=int, help="Number of IPs to be generated")
    args = parser.parse_args()

    for _ in range(int(args.num)):
        print ipaddr.IPAddress(genvalidip())

    return 0

if __name__ == '__main__':
    status = main()
    sys.exit(status)
