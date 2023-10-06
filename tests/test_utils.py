from utils.ip import ip_geo_location, is_cidr, is_ip, is_private_ip


def test_is_private_ip():
    assert is_private_ip(ip="110.242.68.66") is False
    assert is_private_ip(ip="10.0.0.2") is True
    assert is_private_ip(ip="1.1.1.1") is False


def test_is_ip():
    assert is_ip(ip="110.242.68.66") is True
    assert is_ip(ip="110.242.68.668") is False


def test_is_cidr():
    assert is_cidr(cidr="110.242.68.0/24") is True
    assert is_cidr(cidr="110.242.68.0/40") is False


def test_ip_geo_location():
    ip = "110.242.68.66"
    assert "CN" in ip_geo_location(ip=ip)
