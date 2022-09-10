# Script for DNS enumeration

import dns.resolver
import sys

if len(sys.argv) < 2:
    print('Usage: dns_recon.py target.com')
    exit(128)
else:
    target=sys.argv[1]


dnsIP='8.8.8.8'

try:
    answers = dns.resolver.resolve(target, 'A')
except:
    dnsIP='1.1.1.1'

my_resolver = dns.resolver.Resolver()
my_resolver.nameservers = [dnsIP]

def main():
    print(f'Starting dump on: {target}')
    print('-' * 20)
    full_scan(['A', 'TXT', 'MX', 'CNAME', 'AAAA'])
    print('-' * 20)

def full_scan(queries):
    print(f'- DNS Server: {dnsIP}')
    print('\n')

    for query in queries:
        try:
            result = dns.resolver.resolve(target, query)
            for exdata in result:
                print(f'- {query} Record:', exdata)
        except:
            print(f'- No {query} Records')

        print('\n')

main()