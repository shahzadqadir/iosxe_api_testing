from requests import Session


class APIConnectivity:
    def __init__(self, username: str, password: str, **kwargs):
        self.session = Session()
        self.session.auth = (username, password)
        self.session.verify = False
        self.session.headers.update({
            "Accept": "application/yang-data+json",
            "Content-Type": "application/yang-data+json"
            })
