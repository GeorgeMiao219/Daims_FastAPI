import dataset
import logging
import config as cf
from utils import Singleton
logger = logging.getLogger("daims")


@Singleton
class DB(dataset.Database):
    def __init__(self, username, password):
        self.logger = logging.getLogger("daims")
        self.logger.info(f"Id for current DB: {id(self)}")
        self.username = username
        self.pw = password
        self.ip = cf.db_ip if cf.db_ip else "127.0.0.1"
        try:
            super().__init__(f"mysql+pymysql://{self.username}:{self.pw}@{self.ip}:3306/auth")
        except Exception as e:
            logger.warning("Unable to connect to the Database")
            logger.warning(e)

        self.logger.info(f"Database connected to {self.username}@{self.ip}")
