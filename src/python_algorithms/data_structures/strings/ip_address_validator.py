"""
Ip address validator implementation in Python.
"""
class IpAddressValidator:

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
        elif self.is_valid_ipv6(ip):
            return "IPv6"
        else:
            return "Neither"
