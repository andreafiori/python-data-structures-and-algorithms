"""
Ip address validator implementation in Python.
It works for both IPv4 and IPv6 formats.
IP4 address example: 128.0.0.1 See: https//wikipedia.org/wiki/IPv4
IP6 address example: 2001:0db8:85a3:0000:0000:8a2e:0370:7334 See: https//wikipedia.org/wiki/IPv6
"""
class IpAddressValidator:
    """ Class to validate IP addresses with different formats. """

    def is_valid_ipv4(self, ip: str) -> bool:
        parts = ip.split('.')
        if len(parts) != 4:
            return False
        for part in parts:
            if not part.isdigit() or not 0 <= int(part) <= 255 or (part[0] == '0' and len(part) > 1):
                return False
        return True

    def is_valid_ipv6(self, ip: str) -> bool:
        parts = ip.split(':')
        if len(parts) != 8:
            return False
        for part in parts:
            if len(part) == 0 or len(part) > 4 or not all(c in '0123456789abcdefABCDEF' for c in part):
                return False
        return True

    def validate_ip_address(self, ip: str) -> str:
        if self.is_valid_ipv4(ip):
            return "IPv4"
        return "IPv6" if self.is_valid_ipv6(ip) else "Neither"
