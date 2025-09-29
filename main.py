from requests import Session
from api_connectivity import APIConnectivity

if __name__ == "__main__":

    conn = APIConnectivity(username="script", password="cisco123")
    resp = conn.session.get("https://10.10.99.1/restconf/data/netconf-state/capabilities")
    resp2 = conn.session.get("https://10.10.99.1/restconf/data/Cisco-IOS-XE-interfaces-oper:interfaces")
    print(resp.status_code, resp.text)
    print(resp2.status_code, resp2.text)