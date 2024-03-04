from user import User
from requests import Session as BSession
from requests.adapters import HTTPAdapter
from requests.auth import HTTPBasicAuth

class Session(User):

    def __init__(self, username, password, url):
        super().__init__(username, password)
        self._url = url
        self._session = self.create_session()
        

    def create_session(self):
        # create a requests session object
        # The B refers to Built-in module
        s = R=BSession()
        s.auth = HTTPBasicAuth(self.username, self.password)
        # mount the adapter to the session
        s.mount('http://', HTTPAdapter(max_retries=3))
        s.mount('https://', HTTPAdapter(max_retries=3))
        return s
    
    @property
    def get_session(self):
        return self._session
    
    @property
    def url(self):
        return self._url
    
    @url.setter
    def url(self, url):
        self._url = url

    @property
    def username(self):
        return self._username
    
    @property
    def password(self):
        return self._password

    
    

    
