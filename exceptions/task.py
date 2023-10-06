class DongFengException(Exception):
    pass


class HTTPException(DongFengException):
    pass


class InvalidIP(DongFengException):
    pass


class InvalidCIDR(DongFengException):
    pass
