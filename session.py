from user import User
from requests import Session as BSession
from requests.adapters import HTTPAdapter
from requests.auth import HTTPBasicAuth

class Session():

    def __init__(self, user: User, url: str):
        """
        initialize the session with 
        user : Type User
        url : Type str
        session : List of Session and status_code 
        """
        # check if the user is an instance of User and url is a string
        if not isinstance(user, User):
            raise ValueError('user must be an instance of User')
        
        if not isinstance(url, str):
            raise ValueError('url must be a string')
        
        # initialize the user and url
        self._user = user
        self._url = url
        self._session = self.create_session()
        

    def create_session(self):
        # The B refers to Built-in module to differentiate from the Requests.Session class
        s = R=BSession()
        s.auth = HTTPBasicAuth(self._user.username, self._user.password)
        # mount the adapter to the session
        s.mount('http://', HTTPAdapter(max_retries=3))
        s.mount('https://', HTTPAdapter(max_retries=3))

        status_code = s.get(self._url).status_code

        if status_code != 200:
            raise ValueError('authentication failed or url is not valid')
        
        return [s, status_code]
    
    @property
    def get_session(self):
        self._session[1] = self._session[0].get(self._url).status_code
        if self._session[1] != 200:
            raise ValueError('sessions has expired')
        
        return self._session
    
    @property
    def url(self):
        return self._url

    @property
    def username(self):
        return self._username
    
    @property
    def password(self):
        return self._password
    
    @property
    def get_user(self):
        return self._user

    
    

    
