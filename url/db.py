import dataset
import requests
from os import getenv


class DBService(dataset.Database):
    def __init__(self, username, password, table, local=True, ex_ip=None):
        if not local:
            ip = ex_ip
            print("[+] Using dedicated external ip: {}".format(ex_ip))
        else:
            try:
                ip = self.get_ip()
                print("[+] Automatically detected external IP: {}".format(ip))
            except Exception as e:
                raise DBException("[!] Can't find external IP address")
        if not username:
            username = getenv('DBUSER')
        if not password:
            password = getenv('DBPW')
        if not (username and password):
            raise DBException("[!] Unable to Get Database username & password. Set DBUSER and DBPW to environment.")
        print("[+] Logged in as <{}>".format(username))

        try:
            super().__init__(f"mysql+pymysql://{username}:{password}@{ip}:3306/{table}")
        except Exception as e:
            raise DBException("[!] Unable to connect to the Database")

    @staticmethod
    async def get_ip():
        return requests.get('https://checkip.amazonaws.com').text.strip()


class DBException(Exception):
    pass


if __name__ == "__main__":
    from app import db
    tb = db['url']
    for x in ["a", "b", "c"]:
        data = dict(str=3 * x, url='google.com')
        tb.insert(data)
    print(list(tb.find()))
