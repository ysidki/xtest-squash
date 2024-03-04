"""
This class define the profile of the user
"""

class User:

    def __init__(self, username, password, certificate=None, proxy=None):
        self._username = username
        self._password = password
        self._certificate = certificate
        self._proxy = proxy

    @property
    def username(self):
        return self._username

    @property
    def password(self):
        return self._password

    @username.setter
    def username(self, username):
        self._username = username

    @password.setter
    def password(self, password):
        self._password = password

    @property
    def certificate(self):
        return self._certificate
    
    @certificate.setter
    def certificate(self, certificate):
        self._certificate = certificate

    @property
    def proxy(self):
        return self._proxy
    
    @proxy.setter
    def proxy(self, proxy):
        self._proxy = proxy


    