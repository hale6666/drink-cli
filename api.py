import requests
import json
import csh_ldap as ldap
import vari

with open("api.key") as f:
    API_KEY = f.read().strip()
    """
    This is for security online, so the API key is not publicized.
    """
    f.close()

url='https://webdrink.csh.rit.edu/api/index.php'

def test():
    """
    This is not usually called, other than for testing the API.
    """
    head = {"request": "test/api/{}".format(API_KEY), "api_key": API_KEY}
    ret=requests.get(url,params=head)
    print(ret.text)
    print(ret.json())
    print(ret.json()['message'])

def get_credits(uid):
    """
    This is to return the credits a user has, so that it can be shown on the screen.
    """
    head = {"request": "users/credits/{}".format(uid), "uid": uid, "api_key": API_KEY}
    ret = requests.get(url,params=head)
    if ret.status_code != 200:
        raise ValueError
    else:
        return ret.json()['data']

def get_user_info():
    """
    Gets name, credits, etc.
    """
    head = {"request": "users/info/", "api_key": API_KEY}
    ret = requests.get(url,params=head)
    if ret.status_code != 200:
        raise ValueError
    else:
        return ret.json()['data']

def get_machine_info():
    """
    Gets stock of each machine.
    """
    head = {"request": "machines/stock/"}
    ret = requests.get(url,params=head)
    if ret.status_code != 200:
        raise ValueError
    else:
        return ret.json()['data']

def drop_drink(ib, mach, slot, delay):
    """
    Drops specified drink.
    """
    head = {"request": "drops/drop/{}/{}/{}/{}".format(ib, mach, slot, delay), "ibutton": ib,
            "machine_id": mach, "slot_num": slot, "delay": delay, "api_key": API_KEY}
    ret = requests.post(url,data=head)
    if ret.status_code != 200:
        raise ValueError
    else:
        return ret.json()['message']
