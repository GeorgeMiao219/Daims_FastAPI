import logging
import random
import string
import config as cf
from collections import OrderedDict
from traceback import format_exc
from datetime import datetime
from database import DB
from utils import Singleton


@Singleton
class URLController:
    def __init__(self):
        self.db = DB.get_instance(cf.username, cf.password)
        self.lg = logging.getLogger("daims")
        try:
            self.tb = self.db['url']
        except Exception:
            self.lg.warning("Unable to initialize URLController")
            raise

    def get(self, mapping_str):
        """
        Get an record
        :param mapping_str
        :return OrderedDict((rid: int), (str: str), (url: str), (create_time: datetime.datetime), (hits: int))
        """
        ret = self.build_response()
        try:
            row = self.tb.find_one(mapping_str=mapping_str)
            ret = row if row else ret
            self.db.query(f"UPDATE url set hits = hits + 1 "
                          f"WHERE mapping_str='{mapping_str}'")
        except Exception:
            self.lg.warning(f"Error when trying to find {mapping_str}")
            self.lg.warning(format_exc())
        return ret

    def post(self, url):
        """
        Create a new record
        :param url: original url
        :return List[rid: int, mapping_str: str]
        """
        mapping_str = self.rand_str(cf.mapping_str_len)
        url = self.add_url_protocol(url)
        data = dict(mapping_str=mapping_str, url=url)
        try:
            return [self.tb.insert(data, ensure=True), mapping_str, url]
        except Exception as e:
            self.lg.warning(f"Unable to insert data: {data}")
            return [None, e]

    def put(self, mapping_str: str, url: str):
        """
        :param mapping_str: the old mapping_str that's going to assigned to a new url
        :param url: The new url
        :return:
        """
        data = dict(mapping_str=mapping_str, url=url)
        self.db.update(data, ["mapping_str"], ensure=True)

    def delete(self, mapping_str):
        """
        Delete an existing record
        :param mapping_str:
        :return: <bool: is_successful>
        """
        return self.tb.delete(mapping_str=mapping_str)

    @staticmethod
    def build_response(rid: int = None,
                       mapping_str: str = None,
                       url: str = None,
                       create_time: datetime = None,
                       hits: int = None):
        return OrderedDict(rid=rid,
                           mapping_str=mapping_str,
                           url=url,
                           create_time=create_time,
                           hits=hits)

    @staticmethod
    def rand_str(length):
        return ''.join(random.sample(string.ascii_letters + string.digits, length))

    @staticmethod
    def add_url_protocol(url: str, protocol="https://"):
        if url.find("http://") == -1 and url.find("https://") == -1:
            return protocol + url
        else:
            return url
