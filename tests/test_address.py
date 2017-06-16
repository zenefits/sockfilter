from nose.tools import eq_ as equals
from sockfilter import Address


def test_address_to_str():
    to_str = str(Address('/dev/log'))
    equals(to_str, "<Address host: 'None', port: 'None', path: '/dev/log'>")

    to_str = str(Address(('https://localhost', 80)))
    equals(to_str, "<Address host: 'https://localhost', port: '80', path: 'None'>")

    to_str = str(Address(('https://google.com', 443)))
    equals(to_str, "<Address host: 'https://google.com', port: '443', path: 'None'>")
