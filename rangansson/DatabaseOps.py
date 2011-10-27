import ConfigParser
import re
import psycopg2

class NoDefaultValueError(BaseException):
    def __init__(self,message=None):
        BaseException.__init__(self,message)

class DatabaseOps(object):
    def __init__(self):
        self._cursor = None

    def create_configparser(self):
        """
        If the values in etc/database.cfg are not set, this asks the user for
        suitable values
        """
        pass

    def _ask(self, config, *args):
        try:
            value = config.get(*args)
            if re.match('<.*>', value): raise NoDefaultValueError
        except NoOptionError, NoDefaultValueError:
            # Ask the user for his input
            raise NotImplementedError

    def read_config(self, config_filename):
        """
        Read the config file and create a cursor
        """
        config = ConfigParser.RawConfigParser()
        config.read(config_filename)
        hostname = self._ask(config, 'database', 'hostname')
        databasename = self._ask(config, 'database', 'databasename')
        username = self._ask(config, 'database', 'username')
        password = self._ask(config, 'database', 'password')
        #TODO update the sql string to handle missing values
        self.sql_string = """host='%s' dbname='%s' user='%s' password='%s'""" \
                % (hostname, databasename, username, password)



    def _cursor(self):
        """
        Initialize the cursor
        """
        pass

