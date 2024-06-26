import psycopg as pg
import environs
from src.utils import ROOT_DIR

env = environs.Env()

env.read_env(str(ROOT_DIR / '.env'))

class Database(object):
    __instance = None

    def __new__(cls):
        if Database.__instance is None:
            Database.__instance = super().__new__(cls)
            Database.__instance.__init__()

        return Database.__instance.__conn    


    def __init__(self) -> None:
        self.__conn = pg.connect(
            dbname = env.str('db_name'),
            user = env.str('db_user'),
            password = env.str('db_password')

        )


if   __name__ == '__main__' :
    conn = Database()
    print(conn)