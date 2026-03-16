from python_algorithms.data_structures.strings.ip_address_validator import IpAddressValidator

class TestIpAddressValidator:

    def setup_class(self):
        self.ip_validator = IpAddressValidator()

    def test_valid_ipv4(self):
        ip = "192.168.1.1"
        assert self.ip_validator.is_valid_ipv4(ip) == True

    def test_invalid_ipv4(self):
        ip = "256.256.256.256"
        assert self.ip_validator.is_valid_ipv4(ip) == False

    def test_valid_ipv6(self):
        ip = "2001:0db8:85a3:0000:0000:8a2e:0370:7334"
        assert self.ip_validator.is_valid_ipv6(ip) == True

    def test_invalid_ipv6(self):
        ip = "2001:0db8:85a3:0000:0000:8a2e:0370:733g"
        assert self.ip_validator.is_valid_ipv6(ip) == False

    def test_validate_ip_address_ipv4(self):
        ip = "192.168.1.1"
        assert self.ip_validator.validate_ip_address(ip) == "IPv4"

    def test_validate_ip_address_ipv6(self):
        ip = "2001:0db8:85a3:0000:0000:8a2e:0370:7334"
        assert self.ip_validator.validate_ip_address(ip) == "IPv6"
